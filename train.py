from utils import load_coco_data
import ipdb

def main():
    # load train dataset
    data = load_coco_data(data_path='./data', split='train')
    ipdb.set_trace()
    word_to_idx = data['word_to_idx']
    # load val dataset to print out bleu scores every epoch
    val_data = load_coco_data(data_path='./data', split='val')


if __name__ == "__main__":
    main()
