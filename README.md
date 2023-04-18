<!-- *** Based on this template -> https://github.com/othneildrew/Best-README-Template/blob/master/README.md  -->

<a name="readme-top"></a>
<!-- SUMMARY -->

# ChatGPT-my-doc
## What is it?
Script that leverages the the OpenAI GPT-3 text-davinci-003 model so you can query a personal document.

## How do I run it?

First of all, get an OpenAI key from [here](https://platform.openai.com/account/api-keys).
You will have around £20 of free credits which are required to run the model and use the user prompts. You'll find that is plenty just for one person.

 Pop that OpenAI key in this part of the code
 
 ```
os.environ['OPENAI_API_KEY'] = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
```

then add the path to your doc here
 
 ```
documents = loader.load_data(file=Path('testdoc.docx'))

```

![image](https://user-images.githubusercontent.com/43473952/232837380-9eb65b61-2ea1-4569-9bf6-9f2e8c412d19.png)


  
### Further reading 
[LlamaIndex](https://gpt-index.readthedocs.io/en/latest/index.html)
  

<p align="right">(<a href="#readme-top">back to top</a>)</p>



 



 
