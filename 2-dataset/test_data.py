import os
import unittest
import pandas as pd


tot_num = 25_000
os.chdir("/mnt/g/AI/AI2/2-dataset")

class TestData(unittest.TestCase):
    # begin (generated by Sider)
    columns = pd.Index(["text", "label"])  # 添加默认的 columns 属性
    # end (generated by Sider)
    @classmethod
    def setUpClass(cls):
        cls.test = pd.read_parquet("data/test.parquet")
        cls.train = pd.read_parquet("data/train.parquet")
        cls.train_size = int(tot_num * 0.9)
        cls.test_size = tot_num - cls.train_size
        cls.columns = pd.Index(["text", "label"])

    def _test_data(self, data: pd.DataFrame, size: int):
        self.assertTrue(all(data.columns == self.columns))

        target_size = len(data)
        self.assertEqual(target_size, size)

        labels = data["label"].unique()
        self.assertTrue(all(labels == [0, 1]))

        label_sizes = []
        for label in labels:
            label_size = len(data[data["label"] == label])
            label_sizes.append(label_size)
        self.assertTrue(all([label_size == size // 2 for label_size in label_sizes]))

    def test_test_data(self):
        self._test_data(self.test, self.test_size)

    def test_train_data(self):
        self._test_data(self.train, self.train_size)


if __name__ == "__main__":
    unittest.main()
