import argparse
from scripts.plant import plant
from scripts.squeeze import squeeze
from scripts.hydrate import hydrate
from scripts.sniff import sniff
from scripts.preservethaw import thaw, preserve
from scripts.rind import rind
from scripts.ripen import ripen
from scripts.nutrition import nutrition
from scripts.wash import wash

def cmdparse():

    parser = argparse.ArgumentParser(prog="melon")
    sub = parser.add_subparsers(dest='cmd')

    p = sub.add_parser("plant")
    p.add_argument("package", nargs="+")

    p = sub.add_parser("squeeze")
    p.add_argument("package", nargs="+")

    p = sub.add_parser("sniff")
    p.add_argument("query")

    p = sub.add_parser("hydrate")

    p = sub.add_parser("preserve")
    p.add_argument("package", nargs="+")

    p = sub.add_parser("thaw")
    p.add_argument("package", nargs="+")

    p = sub.add_parser("rind")
    p.add_argument("package")

    p = sub.add_parser("nutrition")
    p.add_argument("package")

    p = sub.add_parser("ripen")

    p = sub.add_parser("wash")
    p.add_argument("package")


    args = parser.parse_args()

    match args.cmd:
        case "plant":
            install(args.package)
        case "squeeze":
            squeeze(args.package)
        case "sniff":
            sniff(args.query)
        case "hydrate":
            hydrate()
        case "preserve":
            preserve(args.package)
        case "thaw":
            thaw(args.package)
        case "rind":
            rind(args.package)
        case "nutrition":
            nutrition(args.package)
        case "ripen":
            ripen()
        case "wash":
            wash(args.package)
        case _:
            parser.print_help()

