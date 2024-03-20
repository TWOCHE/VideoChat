# VideoChat Application


The purpose of this application is to provide the opportunity to chat via video. 
The user will have the opportunity to be informed about the video and the content mentioned and will be able to ask questions, without having to open this video and watch it from beginning to end. 
This application has two basic elements. The first is the possibility of video chat via YouTube or Bilibili URLs, and the second is to enter the text to search on YouTube.
This content consists of 4 files. 

videohelper.py file: prepared for video and audio processing
youtubevideo.py file: contains the class structure that will help define a data model
raghelper.py file: using the RAG method on transcribed texts
app.py file: Going live via streamlit application by associating all components with each other using text and audio operations
