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
![image](https://github.com/user-attachments/assets/d7a9b6b5-ac38-4a12-9809-6a112eff366d)

Guide to creating arrows:
first part should be what kind of an arrow it should be 
`->` means a dispatch arrow
`<-` measn a return arrow

This is followed by the source and target 
therefore, `->/user/front` means to draw a dispatch arrow from user to frontend

This is then followed by the label of the arrow:
therefore, `->/user/front/filler text from user to frontend` means to draw a dispatch arrow from user to frontend with the label 'filler text from user to frontend'
