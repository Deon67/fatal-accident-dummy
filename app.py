import streamlit as st
import pickle
a=['harm_env_Curb','harm_env_Ditch','harm_env_EM',
 'harm_env_Other','harm_env_OverTurn','harm_env_Pedestrian','harm_env_SRV','harm_env_Trees','state_Alabama','state_Alaska',
 'state_Arizona','state_Arkansas','state_California','state_Colorado','state_Connecticut', 'state_Delaware',
 'state_District of Columbia','state_Florida','state_Georgia','state_Hawaii','state_Idaho','state_Illinois','state_Indiana','state_Iowa','state_Kansas','state_Kentucky',
'state_Louisiana','state_Maine','state_Maryland','state_Massachusetts','state_Michigan','state_Minnesota','state_Mississippi','state_Missouri','state_Montana',
 'state_Nebraska',
 'state_Nevada',
 'state_New Hampshire',
 'state_New Jersey',
 'state_New Mexico',
 'state_New York',
 'state_North Carolina',
 'state_North Dakota',
 'state_Ohio',
 'state_Oklahoma',
 'state_Oregon',
 'state_Pennsylvania',
 'state_Rhode Island',
 'state_South Carolina',
 'state_South Dakota',
 'state_Tennessee',
 'state_Texas',
 'state_Utah',
 'state_Vermont',
 'state_Virginia',
 'state_Washington',
 'state_West Virginia',
 'state_Wisconsin',
 'state_Wyoming',
 'man_coll_NoCol',
 'man_coll_Rear',
 'man_coll_angle',
 'man_coll_headOn',
 'man_coll_sideswipe',
 'weather_blowingSand',
 'weather_blowingSnow',
 'weather_clear',
 'weather_couldy',
 'weather_crosswinds',
 'weather_drizzle',
 'weather_fog',
 'weather_other',
 'weather_rain',
 'weather_sleet',
 'weather_snow',
 'weather_unknown',
 'weather_unreported']



import numpy as np
b=[]
st.write('# Fatal Accidents')
st.write('## Batch 22 Deeksha S & Dinesh M')
for i in a:
    col1=st.selectbox(i,(1,0))
    b.append(col1)

#col2=st.selectbox('Cross Winds Yes=1,No=0',(1,0))
#col3=st.selectbox('Drizzle Yes=1,No=0',(1,0))
#col4=st.selectbox('Coll HeadOn Yes=1,No=0',(1,0))
#col5=st.selectbox('Minnesota State Yes=1,No=0',(1,0))

model=pickle.load(open('LDA.pkl','rb'))
a=st.button('Predict')
if a:
    if model.predict(np.array(b).reshape(1,-1))==0:
        st.write('The Person is who met with an accident is drunk')
    else:
        st.write('The Person is who met with an accident is  not drunk')


