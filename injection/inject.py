from jinja2 import Template

#create a variable name and open the html file. here file is the variable we are using
file = open("templates/index.html","r")
#read the file and store it in a variable called content
content = file.read()
#close the file
file.close()
print (content)

template = Template(content)
inject = {
    "total_money": 1000000,
    "rent": 300000,
    "groceries": 50000,
    "transportation": 20000,
    "utilities": 10000,
    "entertainment": 15000
}

# template.render(total_money = 1000000)
modified_content = template.render(inject)   
print (modified_content)

file = open("html/index.html","w")
file.write(modified_content)
file.close()