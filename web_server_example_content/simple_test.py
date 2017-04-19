#!/Users/john/anaconda/bin/python3
print("Content-Type: text/html")  # HTML is following
print()  # blank line, end of headers

print('Hey, this is NOT working right!')
print("""
I used the command "python3 -m http.server --cgi" to launch this test web server.
but by default, it will only RUN dynamic web scripts if they are located inside
a subdirectory called 'cgi-bin' or 'htbin'.

Therefore, it is just sending this entire file to the web browser as text.
""")

