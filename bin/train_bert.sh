export BERT_BASE_DIR=/Users/henry/Documents/application/bert/data/chinese_roberta_wwm_ext_L-12_H-768_A-12
export MY_DATASET=/Users/henry/Documents/application/bert/data/
export BPYTHONUNBUFFERED=1

nohup python3 run_multilabel_classifier.py \
--do_train=true \
--do_eval=true \
--do_predict=false \
--data_dir=$MY_DATASET \
--task_name=comment \
--vocab_file=$BERT_BASE_DIR/vocab.txt \
--bert_config_file=$BERT_BASE_DIR/bert_config2.json \
--output_dir=$MY_DATASET/comment_model \
--init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
--max_seq_length=512 \
--train_batch_size=16 \
--learning_rate=5e-5 \
--num_train_epochs=4.0 \
--eval_batch_size=16 >nohup_train.out &

