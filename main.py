from data import build_corpus
from evaluate import hmm_train_eval,crf_train_eval,bilstm_train_and_eval
from utils import extend_maps,prepocess_data_for_lstmcrf

def main():
    """模型训练与评估"""

    # 读取数据
    print("读取数据中...")
    train_word_lists,train_tag_lists,word2id,tag2id = build_corpus("train")
    dev_word_lists,dev_tag_lists = build_corpus("dev",make_vocab=False)
    test_word_lists,test_tag_lists = build_corpus("test",make_vocab=False)

    # 训练并评估hmm模型
    # print("正在训练评估HMM模型")
    # hmm_pred = hmm_train_eval(
    #     (train_word_lists,train_tag_lists),
    #     (test_word_lists,test_tag_lists),
    #     word2id,
    #     tag2id
    # )

    # 训练并评估crf模型
    # crf_pred = crf_train_eval(
    #     (train_word_lists,train_tag_lists),
    #     (test_word_lists,test_tag_lists)
    # )

    # 训练并评估bilstm模型
    # bilstm_word2id, bilstm_tag2id = extend_maps(word2id, tag2id, for_crf=False)
    # lstm_pred = bilstm_train_and_eval(
    #     (train_word_lists, train_tag_lists),
    #     (dev_word_lists, dev_tag_lists),
    #     (test_word_lists, test_tag_lists),
    #     bilstm_word2id, bilstm_tag2id,
    #     crf=False
    # )

    print("正在训练评估Bi-LSTM+CRF模型...")
    # 如果是加了CRF的lstm还要加入<start>和<end> (解码的时候需要用到)
    crf_word2id, crf_tag2id = extend_maps(word2id, tag2id, for_crf=True)
    print(' '.join([i[0] for i in crf_tag2id.items()]))
    # 还需要额外的一些数据处理
    train_word_lists, train_tag_lists = prepocess_data_for_lstmcrf(
        train_word_lists, train_tag_lists
    )
    dev_word_lists, dev_tag_lists = prepocess_data_for_lstmcrf(
        dev_word_lists, dev_tag_lists
    )
    test_word_lists, test_tag_lists = prepocess_data_for_lstmcrf(
        test_word_lists, test_tag_lists, test=True
    )
    lstm_crf_pred = bilstm_train_and_eval(
        (train_word_lists, train_tag_lists),
        (dev_word_lists, dev_tag_lists),
        (test_word_lists, test_tag_lists),
        crf_word2id, crf_tag2id
    )


if __name__ == '__main__':
    main()