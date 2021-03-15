
import fire

from utils import load_model


def main(model_path, text):
    classifier = load_model(model_path=model_path)
    result = classifier.predict(text)
    print(result)


if __name__ == '__main__':
    fire.Fire(main)
