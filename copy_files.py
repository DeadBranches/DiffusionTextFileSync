import os
import argparse

def copy_files(input_dir, reference_dir, alternate_reference_dir, verbose=False):

    for filename in os.listdir(input_dir):
        if not filename.endswith('.png'):
            continue

        input_file = os.path.join(input_dir, filename)
        reference_txt = os.path.join(reference_dir, filename[:-3] + 'txt')
        alternate_reference_txt = os.path.join(alternate_reference_dir, filename[:-3] + 'txt')
        output_txt = os.path.join(input_dir, filename[:-3] + 'txt')

        if os.path.exists(output_txt):
            if verbose:
                print(f"Text exists for {filename}")
            continue

        if os.path.exists(reference_txt):
            with open(reference_txt, 'rb') as src, open(output_txt, 'wb') as dst:
                dst.write(src.read())

            if verbose:
                print(f"Copied {reference_txt} to {input_dir}")
        elif os.path.exists(alternate_reference_txt):
            with open(alternate_reference_txt, 'rb') as src, open(output_txt, 'wb') as dst:
                dst.write(src.read())

            if verbose:
                print(f"Copied text file for to {filename}")
        else:
            print("NONO")

def main():
    parser = argparse.ArgumentParser(description='Copy text files corresponding to PNG files from reference directory or alternate reference directory to input directory')
    parser.add_argument('input_dir', help='input directory containing PNG files')
    parser.add_argument('reference_dir', help='reference directory containing the corresponding text files')
    parser.add_argument('alternate_reference_dir', help='alternate reference directory containing the corresponding text files')
    parser.add_argument('-v', '--verbose', action='store_true', help='enable verbose output')
    args = parser.parse_args()

    copy_files(args.input_dir, args.reference_dir, args.alternate_reference_dir, args.verbose)

if __name__ == '__main__':
    main()
