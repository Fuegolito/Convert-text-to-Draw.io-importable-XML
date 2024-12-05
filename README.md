This is a tool that helps a user to convert some syntactical text into a specific type of XML that is read by draw.io to create a sequence diagram.

For example : 

Setup config like : `title/test;user/x;front/Frontend;back/Backend;ai/AI`
And a sequence of commands like this : 
`->/user/front/filler text from user to frontend,
->/front/back/filler text from frontend to backend,
->/back/ai/filler text from backend to ai,
<-/ai/back/filler text from ai to backend,
<-/back/front/filler text from backend to frontend,
->/front/back/filler text from frontend to backend,
<-/back/front/filler text from backend to frontend,
->/front/user/filler text from frontend to user`

will yield something like: 
![image](https://github.com/user-attachments/assets/23b857b7-4efc-4350-84cb-8f0415ad3695)

Guide to createing setup config:
//TODO

Guide to creating arrows:
first part should be what kind of an arrow it should be 
`->` means a dispatch arrow
`<-` measn a return arrow

This is followed by the source and target 
therefore, `->/user/front` means to draw a dispatch arrow from user to frontend

This is then followed by the label of the arrow:
therefore, `->/user/front/filler text from user to frontend` means to draw a dispatch arrow from user to frontend with the label 'filler text from user to frontend'

This is further followed by a messaging sequence that for now has allows 2 messages to be diplayed with each arrow 
