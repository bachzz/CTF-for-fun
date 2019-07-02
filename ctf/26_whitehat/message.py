import skvideo.io
#import skvideo.datasets
#videodata = skvideo.io.vread(skvideo.datasets.bigbuckbunny())
videodata = skvideo.io.vread("./Message.mpg", num_frames=30)
print(videodata.shape)
