import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset
import os

def extract_filename_without_extension(file_path):
    # Get the base name of the file (including extension)
    file_name_with_extension = os.path.basename(file_path)

    # Split the file name and extension
    file_name, file_extension = os.path.splitext(file_name_with_extension)

    return file_name

def write_string_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-small"
# model_id = "openai/whisper-large"
# model_id = "openai/whisper-large-v3"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=30,
    batch_size=16,
    return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
)

# dataset = load_dataset("distil-whisper/librispeech_long", "clean", split="validation")
# sample = '/home/ubuntu/workspace/akash/ai_apps/coqui/other_wavfiles/Audio-200TCs/Boston01-10.m4a'
# sample = '/home/ubuntu/workspace/akash/ai_apps/coqui/other_wavfiles/aditya/P231213-01342_200/waves/WestCoast01-10-16K-.wav'

# output_folder = "/home/ubuntu/workspace/akash/ai_apps/coqui/other_wavfiles/aditya/P231213-01342_200/waves/whisper_medium/"
# samples = ['Boston01-10-16K-.wav' , 'NY01_10-16K-.wav', 'Northern01-10-16K-.wav',  'Southern01-10-16K-.wav'  ,'WestCoast01-10-16K-.wav'  ,'Boston11-35-16K-.wav' , 'NY11_69-16K-.wav',  'Northern11-44-16K-.wav'  ,'Southern11-49-16K-.wav']
# # for sample in samples:
# sample2 = '/home/ubuntu/workspace/akash/ai_apps/coqui/other_wavfiles/aditya/P231213-01342_200/waves/'+sample
# filename_without_extension = extract_filename_without_extension(sample2)
# output_folder2 = output_folder+filename_without_extension
# print(output_folder)
sample = './audios/sample.wav'
result = pipe(sample)
print(result["text"])
# write_string_to_file(output_folder2, result["text"])