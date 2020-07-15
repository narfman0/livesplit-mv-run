import argparse

from livesplit_mv_run import splits_parser


def mv_run(src_path, dst_path, src_run, dst_run):
    split_src = splits_parser(src_path)
    split_dst = splits_parser(dst_path)
    # TODO move run # from src to dst and write dst


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--src_path")
    parser.add_argument("--dst_path")
    parser.add_argument("--src_run", type=int)
    parser.add_argument("--dst_run", type=int)
    args = parser.parse_args()
    mv_run(args.src_path, args.dst_path, args.src_run, args.dst_run)


if __name__ == "__main__":
    main()