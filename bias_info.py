from Bias import Bias
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", help="")
    parser.add_argument("--test")
    args = parser.parse_args()

    Bias(args.data, model_path="saved_model/vanilla/hate", test_data_path=args.test)

