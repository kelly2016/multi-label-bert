export BERT_BASE_DIR=/home/student/project/kelly/bert/data/chinese_roberta_wwm_ext_L-12_H-768_A-12
export MY_DATASET=/home/student/project/kelly/bert/data/
export BPYTHONUNBUFFERED=1

python3 /home/student/project/kelly/bert/run_multilabel_classifier.py \
--do_predict=true \
--data_dir=$MY_DATASET \
--task_name=comment \
--vocab_file=$BERT_BASE_DIR/vocab.txt \
--bert_config_file=$BERT_BASE_DIR/bert_config2.json \
--output_dir=$MY_DATASET/output \
--init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
--max_seq_length=512
