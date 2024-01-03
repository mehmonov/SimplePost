from openai import OpenAI
client = OpenAI()

def generate_img(prompt):
  response = client.images.generate(
    model="dall-e-2",
    prompt=f"I am writing a telegram post. and you prepare a picture for me according to the tariff of this post. post: {prompt}",
    size="1024x1024",
    quality="standard",
    n=1,
    
  )

  image_url = response.data[0].url
  return image_url

