from project_module import project_object, image_object, link_object, challenge_object

p = project_object('accelerator_future_prospects', 'Accelerator future prospects')
p.domain = 'http://www.aidansean.com/'
p.path = ''
p.preview_image_ = image_object('http://placekitten.com.s3.amazonaws.com/homepage-samples/408/287.jpg', 408, 287)
p.github_repo_name = 'accelerator_future_prospects'
p.mathjax = True
p.introduction = 'This project was written as part of the content for a talk presented at the International Workshop on Future Linear Colliders to compare the future prospects of the LHC and lepton colliders.  It is shared here in case it is of use for other physicists.'
p.overview = '''This project simply plots a series of graphs.'''


p.challenges.append(challenge_object('Using a TMultigraph in pyroot is not easy.', 'In order to make this work I had to use the <tt>array</tt> module, a step I usually forget!  This macro should save me a few headaches in the future.', 'Resolved.'))
