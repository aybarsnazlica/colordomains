def create_domain_start_end(domains):
    starts = domains[::2]
    ends = domains[1::2]

    return starts, ends


def create_start_end_ranges(starts, ends):
    return [range(int(start), int(end) + 1) for start, end in zip(starts, ends)]


def make_modified_line(line, b_factor_table):
    res_num = int(line[22:26].strip())

    return next(
        (
            line[:61] + b_fac + line[67:]
            for ran, b_fac in b_factor_table.items()
            if res_num in ran
        ),
        f"{line[:61]}00.00{line[67:]}",
    )


def mod_pdb(infile, b_factor_table):
    mod_lines = []

    with open(infile) as handle:
        for line in handle:
            line = line.strip()

            if line[:4] == "ATOM":
                mod_line = make_modified_line(line, b_factor_table)
                mod_lines.append(mod_line)
            else:
                mod_lines.append(line)

    return mod_lines


def write_pdb(mod_lines, outfile):
    with open(outfile, "w") as handle:
        for line in mod_lines:
            handle.write(line + "\n")
