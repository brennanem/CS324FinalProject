import json
import requests
import openai
import os

def finetune(data_filename):
    #set api key
    openai.api_key = "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"
    #upload training data file, and get id
    file_response = openai.File.create(
        file=open(data_filename, "rb"),
        purpose='fine-tune'
    ) 
    file_id = file_response["id"]
    #finetune - following values are current default, we can change them
    #FIGURE OUT WEIGHTS AND BIASES
    response = openai.FineTune.create(
        training_file=file_id,
        model='curie',
        n_epochs=4,
        batch_size=None, #null ~0.2%
        learning_rate_multiplier=None, #depends on batch size (0.05-0.2)
        prompt_loss_wight=0.01,
        suffix='224n-haiku-model'
    )

def main():
    finetune("clean_data.jsonl")

if __name__ == "__main__":
    main()