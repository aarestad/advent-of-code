import re

required_fields = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    # 'cid', optional
}

valid_eye_colors = {
    'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth',
}


def validate_height(hgt: str):
    try:
        (amt, unit) = re.match(r'(\d+)(cm|in)', hgt).groups()

        if unit == 'cm':
            return 150 <= int(amt) <= 193
        if unit == 'in':
            return 59 <= int(amt) <= 76
        return False
    except (AttributeError, ValueError):
        return False


def validate_record(record: dict):
    try:
        return 1920 <= int(record['byr']) <= 2002 and \
               2010 <= int(record['iyr']) <= 2020 and \
               2020 <= int(record['eyr']) <= 2030 and \
               validate_height(record['hgt']) and \
               re.match('^#[0-9a-f]{6}$', record['hcl']) and \
               record['ecl'] in valid_eye_colors and \
               re.match(r'^\d{9}$', record['pid'])
    except (KeyError, ValueError):
        return False


if __name__ == '__main__':
    records = []
    current_record = {}

    with open('input/day4.txt') as passport_file:
        for line in passport_file:
            line = line.strip()

            if line == '':
                records.append(current_record)
                current_record = {}
                continue

            fields = line.split(' ')

            for field in fields:
                (name, val) = field.split(':')

                if name in required_fields:
                    current_record[name] = val

    # don't forget the last record
    records.append(current_record)

    print(sum(1 for r in records if validate_record(r)))
