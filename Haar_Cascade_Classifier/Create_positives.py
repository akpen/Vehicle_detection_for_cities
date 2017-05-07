def create_pos_n_neg():
    """This function creates text file
    to list the path for the 
    Negative image set.
    """ 
    for file_type in ['neg']:
        
        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 60 40\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('neg_bg.txt','a') as f:
                    f.write(line)
					

create_pos_n_neg()