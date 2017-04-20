#!/Users/john/anaconda/bin/python3
#
# simple_dynamic_html.py
# j.weible

# The TOP line is is a special syntax that tells the system
# this file is not plain text, but a program that should be run
# by the program at the specified path (which is my python3
# interpreter).
#
# To run this on your computer, change that path above to point
# to YOUR python3 location.  Or try it with no directory path
# after the !

# When run through a web server, everything the program "prints"
# actually gets sent back to the client web browser.
#
# The next 2 lines tell it the content is HTML.
print("Content-Type: text/html")  # HTML is following
print()  # blank line, end of headers

# This is a valid heading for HTML version 4.01
print("""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">
<html lang="en">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
      <title>A simple HTML document, generated by Python</title>
   </head>
   <body>
""")

# Now we're ready to generate some content dynamically to prove
# that Python is producing the output, not just a static file:

print('<p>')  # Start an HTML paragraph
for x in range(1,101):
    print(x, 'squared is', x**2, '<br>')  # the <br> is a line break in HTML

print('</p>')  # close the HTML paragraph tag to stay valid


# Finish the HTML markup:
print("""
    </body>
</html>
""")