import openai
from openai import OpenAI
client = OpenAI()

openai.api_key = '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'

def generate_post(channel_name: str, channel_topic: str, post_title: str, post_description: str) -> str:
    # OpenAI GPT-3 ga so'rov yuborish
    prompt = f"I am an AI developed by OpenAI. I have been asked to generate a post for a Telegram channel named {channel_name}, which focuses on the topic of {channel_topic}. The post should be titled {post_title} and should align with the following description: {post_description}. Please generate a post that fits this description and is engaging for the channel's audience."
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
      
    )
    post_text = response.choices[0].message.content
    
    
    return post_text
    
# generate_post("kanal","dasturlash","php","php haqida")


