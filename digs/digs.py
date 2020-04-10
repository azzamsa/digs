import argparse
import colorama
import dns.resolver
import dns.exception
import yaml
import pathlib

from colorama import Fore, Style


def main():
    colorama.init()

    parser = argparse.ArgumentParser(description="Optional app description")
    parser.add_argument("domain", type=str, help="Domain Name")
    parser.add_argument("rtype", type=str, help="Record type")
    parser.add_argument("-f", type=str, help="Config path")
    parser.add_argument("--check", action="store_true", help="Assert rdata")

    args = parser.parse_args()
    config = read_conf(args.f)
    dig(args.domain, args.rtype, config, test=args.check)


def read_conf(path):

    if not path:
        current_dir = pathlib.Path().cwd()
        files = current_dir.glob("digs.y*")
        for file_ in files:
            if file_.is_file():
                path = file_

        if not path:
            raise FileNotFoundError()

    with open(path, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError:
            print("Invalid YAML file")


def dig(domain, rtype, config, test=False):
    custom_resolver = dns.resolver.Resolver()

    for server in config["servers"]:
        ip_address = server["ip"]
        hostname = server["hostname"]

        custom_resolver.nameservers = [ip_address]
        try:
            answers = custom_resolver.query(domain, rtype)
            for rdata in answers:
                if test:
                    if str(rdata) == config["test"]:
                        print(
                            Fore.GREEN + f"{ip_address} - {hostname} \n"
                            f"{rdata}" + Style.RESET_ALL
                        )
                    else:
                        print(
                            Fore.RED + f"{ip_address} - {hostname} \n"
                            f"{rdata}" + Style.RESET_ALL
                        )
                if not test:
                    print(f"{ip_address} - {hostname} \n" f"{rdata}")

        except dns.exception.Timeout:
            print(Fore.RED + f"Timeout: {ip_address} - {hostname}" + Style.RESET_ALL)
