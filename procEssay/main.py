from procEssay import preproc as pr
from procEssay import featExt as fe

prep_res = pr.preproc('Where do I begin there wasn’t ever. A time when I was patient. '
                      'I was alway rushing people do something and getting mad cause they '
                      'wouldn’t do it fast enough or go fast enough for me. I would just get '
                      'attitude. That why I cant be patient and now you know why. The end. The '
                      'teaching on the way people coming i.e ???.')
features = fe.featext(prep_res)
print(features)