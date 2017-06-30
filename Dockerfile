FROM ningster/my_naoqi:v1.0

# Pull code from Github
RUN cd $HOME
RUN git clone git://github.com/Ningster/pepper_test.git
RUN cd pepper_test
