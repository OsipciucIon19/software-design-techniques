from abc import ABCMeta, abstractmethod


class AbstractDegree(metaclass=ABCMeta):
    @abstractmethod
    def info(self): pass


class BachelorEngineer(AbstractDegree):
    def info(self):
        print('Bachelor of engineering')

    def __str__(self):
        return 'Bachelor of engineering'


class MasterEngineer(AbstractDegree):
    def info(self):
        print('Master of engineering')

    def __str__(self):
        return 'Master of engineering'


class MasterBusinessAdministration(AbstractDegree):
    def info(self):
        print('Master of business administration')

    def __str__(self):
        return 'Master of business administration'


class ProfileAbstractFactory(object):
    def __init__(self):
        self._degrees = []
        self.create_profile()

    @abstractmethod
    def create_profile(self): pass

    def add_degree(self, degree):
        self._degrees.append(degree)

    def get_degrees(self):
        return self._degrees


class ManagerFactory(ProfileAbstractFactory):
    def create_profile(self):
        self.add_degree(BachelorEngineer())
        self.add_degree(MasterBusinessAdministration())


class EngineerFactory(ProfileAbstractFactory):
    def create_profile(self):
        self.add_degree(BachelorEngineer())
        self.add_degree(MasterEngineer())


class ProfileCreatorFactory(object):
    @classmethod
    def create_profile(cls, name):
        return eval(f'{profile_type}Factory')()


if __name__ == '__main__':
    profile_type = input('Which Profile would you like to create? Manager/Engineer - ')

    profile = ProfileCreatorFactory.create_profile(profile_type)
    print(f'Creating Profile of {profile_type}')
    print('Profile has following degrees:')

    for deg in profile.get_degrees():
        print(f' - {deg}')
