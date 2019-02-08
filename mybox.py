from myboxiterator import MyIterator

class MyBox(object):

    def __init__( self ): 
        self.theItems = list() 
        
    def __str__(self):
        return 'List = {}'.format(self.theItems)

    def __len__( self ): 
        return len(self.theItems)

    def add( self, item ): 
        self.theItems.append( item ) 
        
    def remove( self, item ): 
        assert item in self.theItems 
        idx = self.theItems.index( item ) 
        return self.theItems.pop( idx )

    def contains( self, item ): 
        return item in self.theItems 
    
    def iterator( self ): 
        return MyIterator(self.theItems)
    
