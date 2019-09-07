"""
Em uma compra online, o usuário insere informações de sua receita oftálmica, e nosso sistema deve exibir uma lente que atende a sua necessidade. 
Precisamos captar 4 parâmetros numéricos do usuário. São eles: grau esférico do olho esquerdo, grau esférico do olho direito, grau cilíndrico do olho esquerdo 
e grau cilíndrico do olho direito. A lente Prime só pode ser uma opção para o usuário que tiver grau esférico, seja do olho esquerdo ou do olho direito, entre 
-3 e -12. Além disso, ela só atende até grau cilíndrico -2, porém, se o usuário apresentar grau cilíndrico, ela passa a atender grau esférico entre -3 e -10.
Já a lente Vision é uma opção para quem tem de 0 a -15 de esférico e até -5 de cilíndrico. Quando a lente Prime está disponível, ela deve ser a única exibida 
para o usuário. OBS: O grau limite que o usuário pode inserir é de 0 a -15 para esférico e -6 para cilíndrico e são números iterados de 0,25 em 0,25 
(ex: -0,25; 0; +0,25; etc) 
"""


class GlassStore:
    """ 
    This class represents a Glass Store that recommends lens for specific cases.

    Attributes: 
        prime_lens_available (bool): Indicates whether Prime Lens are available in store. 

    """

    def suggest_lens(self, person):
        """ 
        This method makes lens suggestions based on information provided by a Person.
  
        Parameters: 
            person (Person): An object person with its attributes. 
          
        Returns: 
            None.

        """
        if person.cylindrical_degree['right'] == -6 \
                or person.cylindrical_degree['left'] == -6:
            print('Sorry! Unfortunately, we don\'t have any lens available for you.')
            return

        has_cylindrical_degree = person.cylindrical_degree['left'] != 0 \
            or person.cylindrical_degree['right'] != 0

        if has_cylindrical_degree:
            if (person.spherical_degree['left'] < -3 and person.spherical_degree['left'] < -10) \
                    or (person.spherical_degree['right'] < -3 and person.spherical_degree['right'] < -10):
                print('We recommend Vision Lens')
            elif (person.spherical_degree['left'] <= -3 and person.spherical_degree['left'] >= -10) \
                    and (person.spherical_degree['right'] <= -3 and person.spherical_degree['right']) >= -10:
                if (person.cylindrical_degree['left'] <= 0 and person.cylindrical_degree['left'] >= -2) \
                        and (person.cylindrical_degree['right'] <= 0 and person.cylindrical_degree['right'] >= -2):
                    print('We recommend Prime Lens')
                else:
                    print('We recommend Vision Lens')

        else:
            if (person.spherical_degree['left'] <= -3 and person.spherical_degree['left'] >= -12) \
                    and (person.spherical_degree['right'] <= -3 and person.spherical_degree['right'] >= -12):
                if self.prime_lens_available:
                    print('We recommend Prime Lens')
                else:
                    print('We recommend Vision Lens')
            else:
                print('We recommend Vision Lens')

    def __init__(self, prime_lens_available):
        """ 
        The constructor for GlassStore class. 

        Parameters: 
           prime_lens_available (bool): Indicates whether Prime Lens are available in store. 

        """
        self.prime_lens_available = prime_lens_available


class Person:
    """ 
    This class represents a person with cylindrical and spherical degrees.

    Attributes: 
        spherical_degree (dict): Spherical degrees value for left and right eyes. 
        cylindrical_degree (dict): Cylindrical degrees value for left and right eyes. 

    """
    def increment_degree(self, type, eye):
        """ 
        Increments the spherical or cylindrical degree of one person's eye by 0.25.
    
        Parameters: 
        type (str): Type of degree (spherical or cylindrical) 
        eye (str): Specific eye (left or right) 
    
        Returns: 
        None.

        """
        if type.lower() == 'spherical':
            if eye.lower() == 'right':
                if self.spherical_degree['right'] + 0.25 > 0:
                    print('You have reached the maximum degree for this eye!')
                else:
                    self.spherical_degree['right'] += 0.25
            elif eye.lower() == 'left':
                if self.spherical_degree['left'] + 0.25 > 0:
                    print('You have reached the maximum degree for this eye!')
                else:
                    self.spherical_degree['left'] += 0.25
            else:
                print('Invalid eye!')

        elif type.lower() == 'cylindrical':
            if eye.lower() == 'right':
                if self.cylindrical_degree['right'] + 0.25 > 0:
                    print('You have reached the maximum degree for this eye!')
                else:
                    self.cylindrical_degree['right'] += 0.25
            elif eye.lower() == 'left':
                if self.cylindrical_degree['left'] + 0.25 > 0:
                    print('You have reached the maximum degree for this eye!')
                else:
                    self.cylindrical_degree['left'] += 0.25
            else:
                print('Invalid eye!')

        else:
            print('Invalid type!')

    def decrement_degree(self, type, eye):
        """ 
        Decrements the spherical or cylindrical degree of one person's eye by 0.25.
    
        Parameters: 
        type (str): Type of degree (spherical or cylindrical).
        eye (str): Specific eye (left or right).
    
        Returns: 
        None.
        
        """
        if type.lower() == 'spherical':
            if eye.lower() == 'right':
                if self.spherical_degree['right'] - 0.25 < -15:
                    print('You have reached the minimum degree for this eye!')
                else:
                    self.spherical_degree['right'] -= 0.25
            elif eye.lower() == 'left':
                if self.spherical_degree['left'] - 0.25 < -15:
                    print('You have reached the minimum degree for this eye!')
                else:
                    self.spherical_degree['left'] -= 0.25
            else:
                print('Invalid eye!')

        elif type.lower() == 'cylindrical':
            if eye.lower() == 'right':
                if self.cylindrical_degree['right'] - 0.25 < -6:
                    print('You have reached the minimum degree for this eye!')
                else:
                    self.cylindrical_degree['right'] -= 0.25
            elif eye.lower() == 'left':
                if self.cylindrical_degree['left'] - 0.25 < -6:
                    print('You have reached the minimum degree for this eye!')
                else:
                    self.cylindrical_degree['left'] -= 0.25
            else:
                print('Invalid eye!')

        else:
            print('Invalid type!')

    def set_degree(self, type, eye, value):
        """ 
        Defines the value of spherical or cylindrical degree of one person's eye. Spherical degree ranges from -15 to 0 
        and cylindrical degree ranges from -6 to 0.
    
        Parameters: 
        type (str): Type of degree (spherical or cylindrical) 
        eye (str): Specific eye (left or right) 
        value (flot): Degree value

        Returns: 
        None
        
        """
        if type.lower() == 'spherical':
            if value > 0 or value < -15:
                print('Invalid value for this degree!')
            else:
                if eye.lower() == 'right':
                    self.spherical_degree['right'] = value
                elif eye.lower() == 'left':
                    self.spherical_degree['left'] = value
                else:
                    print('Invalid eye!')

        elif type.lower() == 'cylindrical':
            if value > 0 or value < -6:
                print('Invalid value for this degree!')
            else:
                if eye.lower() == 'right':
                    self.cylindrical_degree['right'] = value
                elif eye.lower() == 'left':
                    self.cylindrical_degree['left'] = value
                else:
                    print('Invalid eye!')

        else:
            print('Invalid type!')

    def __init__(self, spherical_degree, cylindrical_degree):
        """ 
        The constructor for Person class. 

        Parameters: 
           spherical_degree (dict): Indicates whether Prime Lens are available in store. 
           cylindrical_degree (dict): Indicates whether Prime Lens are available in store. 

        """
        self.spherical_degree = spherical_degree
        self.cylindrical_degree = cylindrical_degree

    def __str__(self):
        """ 
        This method is a useful string representation of the object.
  
        Parameters: 
            None.
          
        Returns: 
            None.

        """
        return 'Person --> Spherical Degree - {}, Cylindrical Degree - {}'.format(self.spherical_degree, self.cylindrical_degree)


def main():
    spherical_degree = {}
    cylindrical_degree = {}
    spherical_degree['left'] = -3
    spherical_degree['right'] = -10
    cylindrical_degree['left'] = 0
    cylindrical_degree['right'] = 0

    p = Person(spherical_degree, cylindrical_degree)
    print(p)
    opt = GlassStore(True)
    opt.suggest_lens(p)


if __name__ == '__main__':
    main()
