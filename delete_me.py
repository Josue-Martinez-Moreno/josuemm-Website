def dict_eddyt(ts,eddys,eddydt='',var="",analysis="insideness"):
    '''
    ********************** dict_eddyt **********************
    Create a dictionary with all the eddies and it's track on time. When 'ts==0' 
    or eddydt is not defined it start creating a new dictionary otherwise 
    it grows the dictionary.
    Notes:
        Check for some possible bugs where it's saving more than once some features.
    Args:
        
        ts (int): Step or counter used to move in time.
        eddys (dict): Dictionary containing all the relevant information of 
            the features. Check "dict_eddym".
        eddydt(dict): Output dictionary of this function used to grow the 
            features. Check "dict_eddyt".
        analysis (str): Multiple options to track features on time: 
            indideness: Check the coordenates of the var.max() at time t is inside 
                        close contour at time t+1.
            overlap: Check the overlap between close contours between time t and T+1. 
                     The saved contour is the one which contains the maximum overlap.
            closest: Calculates the distance between maximum values or the center of 
                     mass and correlates the closest features.
        var (matrix): Field analysed, neccessary depending on the analysis used.
    Returns:
    
        eddydt - Dictionary containig each eddy and it's track on time.
        All the keys have the following form:
        {eddyn_0:{neddy,time,position,ellipse,contour,...},
        eddyn_1:{neddy,time,position,ellipse,contour,...},...}
    Usage:
        if tt==0:
            eddytd=dict_eddyt(tt,eddys)
        else:
            eddytd=dict_eddyt(tt,eddys,eddytd) 
        
    '''
    


def dict_eddyt(ts,eddys,eddydt=''):
    '''
    ********************** dict_eddyt **********************
    Create a dictionary with all the eddies and it's track on time. When 'ts==0' or eddydt is not defined it start creating a new dictionary otherwise it grows the dictionary.
    Notes:
        Check for some possible bugs where it's saving more than once some features.
    Args:
        ts (int): Step or counter used to move in time.
        eddys (dict): Dictionary containing all the relevant information of the features. Check "dict_eddym".
        eddydt(dict): Output dictionary of this function used to grow the features. Check "dict_eddyt".
    Returns:
        eddydt - Dictionary containig each eddy and it's track on time.
        All the keys have the following form:
        {eddyn_0:{neddy,time,position,ellipse,contour,...},eddyn_1:{neddy,time,position,ellipse,contour,...},...}
    Usage:
        if tt==0:
            eddytd=dict_eddyt(tt,eddys)
        else:
            eddytd=dict_eddyt(tt,eddys,eddytd) 
        
    '''
    if type(eddys['EddyN'][0])==int and (ts==0 or eddydt==''):
        eddydt={'eddyn_'+str(eddys['EddyN'][0]):{'neddy':eddys['EddyN'][0],'time':np.array([ts]),\
                'position':[eddys['Position'][0]],\
                'area':eddys['Area'][0],'ellipse':[eddys['Ellipse'][0]],'contour':[eddys['Contour'][0]],\
                'angle':eddys['Angle'][0],'position_maxvalue':[eddys['PositionExtreme'][0]],\
                'position_eddy':eddys['PositionEllipse'][0],'level':eddys['Level'][0],\
                'majoraxis':eddys['MajorAxis'][0],'minoraxis':eddys['MinorAxis'][0],\
                '2dgaussianfit':eddys['2DGaussianFit'][0],'timetracking':True}}
    
    elif ts==0 or eddydt=='':
        eddydt={'eddyn_'+str(eddys['EddyN'][0][0]):{'neddy':eddys['EddyN'][0],'time':np.array([ts]),\
                'position':[eddys['Position'][0]],\
                'area':eddys['Area'][0],'ellipse':[eddys['Ellipse'][0]],'contour':[eddys['Contour'][0]],\
                'angle':eddys['Angle'][0],'position_maxvalue':[eddys['PositionExtreme'][0]],\
                'position_eddy':eddys['PositionEllipse'][0],'level':eddys['Level'][0],\
                'majoraxis':eddys['MajorAxis'][0],'minoraxis':eddys['MinorAxis'][0],\
                '2dgaussianfit':eddys['2DGaussianFit'][0],'timetracking':True}}
        
        for nn in range(1,len(eddys['EddyN'])):
            eddydt['eddyn_'+str(eddys['EddyN'][nn][0])]={'neddy':eddys['EddyN'][nn],'time':np.array([ts]),\
                    'position':[eddys['Position'][nn]],\
                    'area':eddys['Area'][nn],'ellipse':[eddys['Ellipse'][nn]],'contour':[eddys['Contour'][nn]],\
                    'angle':eddys['Angle'][nn],'position_maxvalue':[eddys['PositionExtreme'][nn]],\
                    'position_eddy':eddys['PositionEllipse'][nn],'level':eddys['Level'][nn],\
                    'majoraxis':eddys['MajorAxis'][nn],'minoraxis':eddys['MinorAxis'][nn],\
                    '2dgaussianfit':eddys['2DGaussianFit'][nn],'timetracking':True}
    else: 
        checklist=[]
        checklist1=[]
        ceddies=[]

        for key, value in list(eddydt.items()):
            if value['timetracking']==False:
                status='No Tracking'
            else:
                minoraxis= value['minoraxis']
                majoraxis= value['majoraxis']
                number=value['neddy']
                times=value['time']
                position=value['position']
                position_max=value['position_maxvalue']
                position_eddy=value['position_eddy']
                ellipse=value['ellipse']
                contour=value['contour']
                level= value['level']
                gaussianfit=value['2dgaussianfit']
                if isinstance(number, np.float64) or isinstance(number, np.int64) or type(number)==int or type(number)==float:
                    number = number
                else: 
                    number = number[0]
                    
                if len(np.shape(value['position']))<2:
                    eddyxt0=value['position'][0]
                    eddyyt0=value['position'][1]
                    areae=value['area']
                    anglee=value['angle']
                    timee=value['time']
                else:
                    eddyxt0=value['position'][-1][0]
                    eddyyt0=value['position'][-1][1]
                    areae=value['area'][-1]
                    anglee=value['angle'][-1]
                    timee=value['time'][-1]
                
                    if len(np.shape(minoraxis))==3:
                        minoraxis=np.squeeze(minoraxis)
                    if len(np.shape(majoraxis))==3:
                        majoraxis=np.squeeze(majoraxis)
                        
                if type(eddys['EddyN'])== int:
                    maxlon=eddys['Contour'][0][0].max()
                    maxlone=eddys['Ellipse'][0][0].max()
                    maxlat=eddys['Contour'][0][1].max()
                    maxlate=eddys['Ellipse'][0][1].max()
                    minlon=eddys['Contour'][0][0].min()
                    minlone=eddys['Ellipse'][0][0].min()
                    minlat=eddys['Contour'][0][1].min()
                    minlate=eddys['Ellipse'][0][1].min()
                    area=eddys['Area']
                    angle=eddys['Angle']        
                    eddyxt1=eddys['Position'][0]
                    eddyyt1=eddys['Position'][1]
                    
                    if (eddyxt1<=maxlon and eddyxt1>=minlon and eddyyt1<=maxlat and eddyyt1>=minlat) and\
                        (eddyxt0<=maxlon and eddyxt0>=minlon and eddyyt0<=maxlat and eddyyt0>=minlat) and\
                        int(timee)!=ts and (ts-int(timee))<5 and (checklist1!=eddys['EddyN']):
                        ## Last condition added 27 of sepbermber to stop repeating eddies trackings. ##
                        #print(np.vstack((position_max,eddys['PositionExtreme'])))
                        eddydt['eddyn_'+str(number)]={'neddy':number,'time':np.vstack((value['time'],ts)),\
                                            'position':np.vstack((position,eddys['Position'])),\
                                            'position_maxvalue':np.vstack((position_max,eddys['PositionExtreme'])),\
                                            'area':np.vstack((value['area'],area)),'angle':np.vstack((value['angle'],angle)),\
                                            'ellipse':ellipse+[eddys['Ellipse'][0]],\
                                            'contour':contour+[eddys['Contour'][0]],\
                                            'position_eddy':np.vstack((position_eddy,eddys['PositionEllipse'])),\
                                            'level':np.vstack((level,eddys['Level'])),\
                                            'minoraxis':np.vstack((minoraxis,np.squeeze(eddys['MinorAxis'][0]))),\
                                            'majoraxis':np.vstack((majoraxis,np.squeeze(eddys['MajorAxis'][0]))),\
                                            '2dgaussianfit':np.vstack((gaussianfit,eddys['2DGaussianFit'][0])),\
                                            'timetracking':True}
                        
                        checklist1.append(eddys['EddyN'])
                        checklist.append(number)
                    elif (eddyxt1<=maxlon and eddyxt1>=minlon and eddyyt1<=maxlat and eddyyt1>=minlat) and\
                           (eddyxt0<=maxlon and eddyxt0>=minlon and eddyyt0<=maxlat and eddyyt0>=minlat) and\
                        int(timee)!=ts and (ts-int(timee))>=5:
                        #print('Add Removal')
                        eddydt['eddyn_'+str(number)]['timetracking']=False    
                else: 
                    for nn in range(0,len(eddys['EddyN'])):
                        maxlon=eddys['Contour'][nn][0].max()
                        maxlone=eddys['Ellipse'][nn][0].max()
                        maxlat=eddys['Contour'][nn][1].max()
                        maxlate=eddys['Ellipse'][nn][1].max()
                        minlon=eddys['Contour'][nn][0].min()
                        minlone=eddys['Ellipse'][nn][0].min()
                        minlat=eddys['Contour'][nn][1].min()
                        minlate=eddys['Ellipse'][nn][1].min()
                        area=eddys['Area'][nn]
                        angle=eddys['Angle'][nn]  
                        eddyxt1=eddys['Position'][nn][0]
                        eddyyt1=eddys['Position'][nn][1]
                        #print('time_step',np.shape(gaussianfit),np.shape(eddys['2DGaussianFit'][nn]))
                        #print('time',gaussianfit,eddys['2DGaussianFit'][nn])
                        #print(np.shape(minoraxis),np.shape(np.squeeze(eddys['MinorAxis'][nn])))
                        if (eddyxt1<=maxlon and eddyxt1>=minlon and eddyyt1<=maxlat and eddyyt1>=minlat) and\
                            (eddyxt0<=maxlon and eddyxt0>=minlon and eddyyt0<=maxlat and eddyyt0>=minlat) and\
                            int(timee)!=ts and (ts-int(timee))<5 and int(eddys['EddyN'][nn]) not in checklist1:
                            ## Last condition added 27 of sepbermber to stop repeating eddies trackings. ##
                            #print(np.vstack((position_max,eddys['PositionExtreme'][nn])))
                            eddydt['eddyn_'+str(number)]={'neddy':number,'time':np.vstack((value['time'],ts)),\
                                            'position':np.vstack((position,eddys['Position'][nn])),\
                                            'position_maxvalue':np.vstack((position_max,eddys['PositionExtreme'][nn])),\
                                            'area':np.vstack((value['area'],area)),'angle':np.vstack((value['angle'],angle)),\
                                            'ellipse':ellipse+[eddys['Ellipse'][nn]],\
                                            'contour':contour+[eddys['Contour'][nn]],\
                                            'position_eddy':np.vstack((position_eddy,eddys['PositionEllipse'][nn])),\
                                            'level':np.vstack((level,eddys['Level'][nn])),\
                                            'minoraxis':np.vstack((np.squeeze(minoraxis),np.squeeze(eddys['MinorAxis'][nn]))),\
                                            'majoraxis':np.vstack((np.squeeze(majoraxis),np.squeeze(eddys['MajorAxis'][nn]))),\
                                            '2dgaussianfit':np.vstack((gaussianfit,eddys['2DGaussianFit'][nn])),\
                                            'timetracking':True}
                        
                            checklist1.append(int(eddys['EddyN'][nn]))
                            checklist.append(number)
                        elif (eddyxt1<=maxlon and eddyxt1>=minlon and eddyyt1<=maxlat and eddyyt1>=minlat) and\
                            (eddyxt0<=maxlon and eddyxt0>=minlon and eddyyt0<=maxlat and eddyyt0>=minlat) and\
                            int(timee)!=ts and (ts-int(timee))>=5:
                            #print('Add Removal')
                            eddydt['eddyn_'+str(number)]['timetracking']=False
                    
                ceddies.append(number)
                
        counter=0
        checklist2=[]
        checklist3=[]
        for key, value in list(eddydt.items()):
            if value['timetracking']==True:
                number=value['neddy']
                if isinstance(number, np.float64) or isinstance(number, np.int64) or type(number)==int or type(number)==float:
                    number = number
                else: 
                    number = number[0]
                if type(eddys['EddyN'])== int:
                    number1=eddys['EddyN']
                    
                    if number not in  checklist and number1 not in checklist1 and number not in checklist2\
                        and number1 not in checklist3:
                        checklist2.append(number)
                        checklist3.append(number1)
                        counter=counter+1
                        number=np.max(ceddies)+counter
                        if isinstance(number, np.float64) or isinstance(number, np.int64):
                            number = number
                        else: 
                            number = eddys['EddyN'][nn][0]
                        eddydt['eddyn_'+str(number)]={'neddy':number,'time':np.array([ts]),\
                                        'position':eddys['Position'],\
                                        'position_maxvalue':eddys['PositionExtreme'],\
                                        'area':eddys['Area'],'angle':eddys['Angle'],\
                                        'position_eddy':eddys['PositionEllipse'],'ellipse':[eddys['Ellipse'][0]],\
                                        'contour':[eddys['Contour'][0]],'level':eddys['Level'],\
                                        'minoraxis':eddys['MinorAxis'][0],'majoraxis':eddys['MajorAxis'][0],\
                                        '2dgaussianfit':eddys['2DGaussianFit'][0],\
                                        'timetracking':True}
                else:
                    for nn in range(0,len(eddys['EddyN'])):
                        number1=eddys['EddyN'][nn]
                    
                        if number not in checklist and number1 not in checklist1 and number not in checklist2\
                            and number1 not in checklist3:
                            checklist2.append(number)
                            checklist3.append(number1)
                            counter=counter+1
                            number=np.max(ceddies)+counter
                            if isinstance(number, np.float64) or isinstance(number, np.int64):
                                number = number
                            else:
                                number = eddys['EddyN'][nn][0]
                            
                            eddydt['eddyn_'+str(number)]={'neddy':number,'time':np.array([ts]),\
                                        'position':[eddys['Position'][nn]],\
                                        'position_maxvalue':[eddys['PositionExtreme'][nn]],\
                                        'area':eddys['Area'][nn],'angle':eddys['Angle'][nn],\
                                        'position_eddy':eddys['PositionEllipse'][nn],'ellipse':[eddys['Ellipse'][nn]],\
                                        'contour':[eddys['Contour'][nn]],'level':eddys['Level'][nn],\
                                        'minoraxis':eddys['MinorAxis'][nn],'majoraxis':eddys['MajorAxis'][nn],\
                                        '2dgaussianfit':eddys['2DGaussianFit'][nn],\
                                        'timetracking':True}
    return eddydt