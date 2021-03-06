
import numpy as np
from menu_model_short import SearchEnvironment
from pomdp_task import SearchTask
from pybrain.rl.experiments import EpisodicExperiment
from learners.sparse_updated import GP_SARSA_SPARSE
from agents.sparse_agent_menu import GPSARSA_Agent

performance=[]  #reward accumulation, dump variable for any evaluation metric
sum=[]


track_time=[]
dict_size=[]

for repeat in range(1):
    env = SearchEnvironment()  # goal
    task = SearchTask(env,8)
    learner = GP_SARSA_SPARSE(gamma=0.95)
    learner.sigma = 1
    learner.batchMode = False  # extra , not in use , set to True for batch learning
    agent = GPSARSA_Agent(learner)
    agent.logging = True

    exp = EpisodicExperiment(task, agent)
    agent.reset()
    sum=[]
    performance=[]
    track_time=[]
    agent.init_exploration=1
    #starttime = time.time()
    dict_size=[]
    epsilon=[]

    b=[]
    c=[]
    for num_exp in range(1000):
        #print('new episode')
        performance=exp.doEpisodes(1)
        sum = np.append(sum, np.sum(performance))
        if (num_exp % 50 == 0 and num_exp != 0):
            agent.init_exploration -= agent.init_exploration * 0.1
            agent.learn()
            agent.reset()
        avg = np.mean(sum[num_exp-10:num_exp])
        print(sum)
        #if(num_exp%10==0 and num_exp!=0):


        #print(learner.state_dict.shape)
        #dict_size=np.append(dict_size,learner.state_dict.shape[0])
        #track_time=np.append(track_time,[time.time()-starttime])
        #print(track_time)

    #file=open("menu_reward.txt",'w')
    #for some in sum:
    #    file.write("%s \n" %some)
    #print(avg)




