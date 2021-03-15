# fastText

facebook 的 fastText训练、验证以及预测的代码

## install

    pip install -r requirements.txt
    
## prepare dataset

准备数据集如下所示（句子切分代码见**preprocess.py**）：

    __label__Shares , 中铁 物资 最快 今年底 A H股 上市 募资 120 亿 陈 姗姗 募集 资金 100 亿到 120 亿元 央企 中国 铁路 物资 总公司 下称 中铁 物资 希望 2011 年 底
    __label__Furnishing , 选择 合适 防盗门 装修 热季 很多 市民 拿到 新楼 后 都 会 选择 装 上 一道 防盗门 新 家 增加 保障 选择 适合 防盗门
    __label__Sociology , 警察 办公楼 10 层 跳 下 身亡 遗书 称 工作 压力 大 时间 昨日 上午 地点 饶平县 公安局 大楼 职务 饶平县 治安管理 中队 副队长
    
## train 

    python train_eval.py \
        --data_path="static/data.txt" \
        --output_dir="./output" \
        --dim=100 \
        --lr=0.5 \
        --epoch=5 \
        --train_proportion=0.8
   
## predict

    python predict.py \
        --model_path="output/data_dim100_lr00.5_iter5.model" \
        --text="人民币 走 贬 国内 期 市 不 理睬 观点 人民币 贬值 短期 仍 冲抵 外部 需求 减弱 负面影响 美元 信任危机 各国 贸易 保护 抬头 全球 商品 需求 进一步 下降 长期 来看 商品价格 不 乐观"