
import os
import fire

from utils import TransformData, split_train_test
from utils import train_model, cal_precision_and_recall


def main(data_path="static/data.txt",
         output_dir="./output/",
         dim=100,
         lr=0.5,
         epoch=5,
         train_proportion=0.8):

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    _, full_filename = os.path.split(data_path)
    filename, _ = os.path.splitext(full_filename)

    csv_file = os.path.join(output_dir, filename.rsplit('.', 1)[0] + '.csv')

    td = TransformData()
    handler = open(data_path)
    td.to_csv(handler, csv_file)
    handler.close()

    train_file, test_file = split_train_test(csv_file, output_dir, train_proportion=train_proportion)

    model = os.path.join(output_dir, f'data_dim{str(dim)}_lr0{str(lr)}_iter{str(epoch)}.model')

    classifier = train_model(ipt=train_file,
                             opt=model,
                             model=model,
                             dim=dim, epoch=epoch, lr=lr
                             )

    result = classifier.test(test_file)
    print(result)

    cal_precision_and_recall(classifier, test_file)


if __name__ == '__main__':
    fire.Fire(main)