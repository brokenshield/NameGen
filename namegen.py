import random

class NameGen:
    def __init__(self, in_file='names.txt', is_whole=True, is_joiner=False, join_chance=0.5, is_sorted=False, out_file='namegen_output.txt'):
        self.infile = in_file
        self.whole = is_whole
        self.joiner = is_joiner
        self.join_chance = join_chance
        self.sorted = is_sorted
        self.outfile = out_file

    def generator(self):
        '''Suggested improvement: If not fed arguments, request input from the terminal for each of the options.'''
        '''Main method'''    
        input_names = []
        name_chunks = []
        full_name = []
    
        '''STAGE 1: Importing the source names'''
        try:
            print('Importing and cleaning source names from ' + self.infile + ' file...')
            data = self.get_names()
            '''reading the lines one at a time here!'''
            for each_name in data:
                try:
                    '''Remove whitespace from each value'''          
                    each_name = each_name.strip()
                    input_names.append(each_name)
                except ValueError as varr:
                    print('ValueError: ' +str(varr))               
        except IOError as ioerr:
            print('The data file is missing! File error: ' +str(ioerr))

        '''STAGE 2: Use whole names or split into chunks'''
        if self.whole:
            '''If whole_name = True do not split the names into chunks!'''
            chunks = input_names 
        else:
            '''If whole_name = False do split the names into chunks equal in length to chunk_length'''  
            chunks = self.generate_chunks(input_names)
                  
        '''STAGE 3: Randomize chunks and recombine as names'''
        full_name = self.generate_name(chunks)
      
        '''STAGE 4: (Optional) Sort full_names'''
        if self.sorted:
            print('Sorting names alphabetically...')
            full_name = sorted(full_name)
        
        '''STAGE 5: Write the names to the output file'''
        '''Why no pickle? Because the file needs to be human readable :) '''
        try:
            print('Writing to ' + self.outfile + ' file...')
            with open(self.outfile, 'w') as self.outfile:
                for each_name in full_name:
                    '''Prints one name to a line'''
                    print(each_name,file=self.outfile)                
        except IOError as err:
            print('File Error: ' +str(err))


    def get_names(self):
        '''Support method: Expects a file name'''
        try:
            with open(self.infile) as f:
                data = f.readline()
                '''Need to strip out any whitespace from the line and seperate by comma. Individual value whitespace removal done below'''
            return(data.strip().split(','))
        except IOError as ioerr:
            print('File error: ' +str(ioerr))
            return(None)

    def generate_chunks(self, names):
        '''Support method: Expects a list of names.'''
        '''This method is where the names get spliced up into chunks and recombined.'''
        full_chunk = []
        syllable_list = []
        print('Beginning chunk processing...')
        for w in names:
            syllable_list.append(w[:3])
            syllable_list.append(w[3:])
            # TODO: If a syllable is less than 3 characters long, throw it away.
        print(syllable_list)
        full_chunk = []
        for each_chunk in syllable_list:
            '''Takes a first name chunk from the names list and add it to a random second name chunk then returns is. All lowercase.'''
            last_chunk = random.choice(names)
            full_chunk.append(each_chunk.lower() + last_chunk.lower())
        print('Chunks generated...')
        return(full_chunk)
    
    def generate_name(self, names):
        '''Support method: expects a list of names!'''
        full_name = []
        joiners = ['ap', 'di', 'von', 'sa', 'dan', 'shi', 'ven', 'xi', 'wen']
        '''Shuffle up all the names'''
        random.shuffle(names)
        try:
            print('Generating names now...')
            for each_name in names:
                '''Takes a first name from the names list and adds on a random second name. Method also capitalizes both names (but not joiners). '''
                last_name = random.choice(names)
                if self.joiner:
                    '''Select a random value from the joiners list'''
                    joiner = random.choice(joiners)
                    '''Generate up a random % chance for the joiner being used'''
                    r = random.random()
                    '''Even when joiners are allowed there is a default 50% chance they won't be used.'''
                    if r > self.join_chance:
                        full_name.append(each_name.capitalize() + ' ' + joiner + ' ' + last_name.capitalize())
                    else:
                        full_name.append(each_name.capitalize() + ' ' + last_name.capitalize())
                else:
                    full_name.append(each_name.capitalize() + ' ' + last_name.capitalize())
            print('Names successfully generated...')
            return(full_name) 
        except ValueError as verr:
            print('Value error: ' +str(verr))
            return(None)        

'''Call to the class'''        
gethans = NameGen(is_whole=False)
gethans.generator()
