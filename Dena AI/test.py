import openai

openai.api_key_path="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"
response = openai.Image.create_edit(
  image=open("C:\\Users\\gvinay\\Documents\\GitHub\\OpenAI\\Dena AI\\sunlit_lounge.jpeg", "rb"),
  mask=open("C:\\Users\\gvinay\\Documents\\GitHub\\OpenAI\\Dena AI\\mask.jpeg", "rb"),
  prompt="A sunlit indoor lounge area with a pool containing a flamingo",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']