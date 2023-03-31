import argparse
from .classmodule import BFactorRange
from .funcmodule import (
    mod_pdb,
    write_pdb,
    create_domain_start_end,
    create_start_end_ranges,
)


def main():
    parser = argparse.ArgumentParser(
        description="Python command line application to visualize protein domains"
    )
    parser.add_argument("-i", "--input", help="3D protein structure in PDB format")
    parser.add_argument(
        "-o", "--output", help="Modified copy of the input 3D protein structure"
    )
    parser.add_argument(
        "-d",
        "--domains",
        nargs="+",
        help="Protein domain start and end residue numbers (whitespace separated)",
    )
    args = parser.parse_args()

    num_domains = int(len(args.domains) / 2.0)
    starts, ends = create_domain_start_end(args.domains)
    ranges_list = create_start_end_ranges(starts, ends)

    b_factors = BFactorRange(num_domains=num_domains, ranges_list=ranges_list)
    b_factor_table = b_factors.to_table()
    mod_pdb_lines = mod_pdb(args.input, b_factor_table)
    write_pdb(mod_pdb_lines, args.output)


if __name__ == "__main__":
    main()
