from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained(
    "THUDM/chatglm-6b", trust_remote_code=True)
model = AutoModel.from_pretrained(
    "THUDM/chatglm-6b", trust_remote_code=True).half().cuda()

_ = model.save_pretrained("./model")
_ = tokenizer.save_pretrained("./model")
