title=input()
article=input()
print("<h1>\n"
      f"\t{title}\n"
      "</h1>")

print("<article>\n"
      f"\t{article}\n"
      "</article>")
while True:
    comment=input()
    if comment=="end of comments":
        break
    print("<div>\n"
          f"\t{comment}\n"
          "</div>")