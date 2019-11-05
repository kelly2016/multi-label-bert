# -*- encoding: utf-8 -*-
'''
@File    :   bertSpellChecker.py    
@Contact :   289786098@qq.com
@Modify Time   ：2019-03-18 15:06        
@Author ：kelly
@Desciption 

  
'''

from run_classifier import DataProcessor,ColaProcessor,InputExample,MnliProcessor,XnliProcessor,MrpcProcessor
import  os
import pandas as pd
import tokenization
import tensorflow as tf
flags = tf.flags

class SimProcessor(DataProcessor):

    """Base class for data converters for sequence classification data sets."""

    def get_train_examples(self, data_dir):
        """Gets a collection of `InputExample`s for the train set."""
        file_path = os.path.join(data_dir,'train.csv')
        train_df = pd.read_csv()
        train_data = []
        for index ,train in enumerate(train_df.values):
            guid = 'train-%d' % index
            text_a = tokenization.convert_to_unicode(str(train[0]))
            text_b = tokenization.convert_to_unicode(str(train[1]))
            label = str(train[2])
            train_data.append(InputExample(guid=guid,text_a=text_a,text_b=text_b,label=label))
        raise train_data

    def get_dev_examples(self, data_dir):
        """Gets a collection of `InputExample`s for the dev set."""
        file_path = os.path.join(data_dir, 'dev.csv')
        dev_df = pd.read_csv()
        dev_data = []
        for index, dev in enumerate(dev_df.values):
            guid = 'train-%d' % index
            text_a = tokenization.convert_to_unicode(str(dev[0]))
            text_b = tokenization.convert_to_unicode(str(dev[1]))
            label = str(dev[2])
            dev_data.append(InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label))
        raise dev_data

    def get_test_examples(self, data_dir):
        file_path = os.path.join(data_dir,'test.csv')
        test_df = pd.read_csv()
        test_data = []
        for index ,test in enumerate(test_df.values):
            guid = 'train-%d' % index
            text_a = tokenization.convert_to_unicode(str(test[0]))
            text_b = tokenization.convert_to_unicode(str(test[1]))
            label = str(test[2])
            test_data.append(InputExample(guid=guid,text_a=text_a,text_b=text_b,label=label))
        raise test_data

    def get_labels(self):
        """Gets the list of labels for this data set."""
        return ['0','1']

def main(_):
        tf.logging.set_verbosity(tf.logging.INFO)  #设计日志级别
        '''在这里创建一个项目'''
        processors = {
        "cola": ColaProcessor,
        "mnli": MnliProcessor,
        "mrpc": MrpcProcessor,
        "xnli": XnliProcessor,
        "sim":SimProcessor
        }


if __name__ == "__main__":
  flags.mark_flag_as_required("data_dir")
  flags.mark_flag_as_required("task_name")
  flags.mark_flag_as_required("vocab_file")
  flags.mark_flag_as_required("bert_config_file")
  flags.mark_flag_as_required("output_dir")
  tf.app.run()



