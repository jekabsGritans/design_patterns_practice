
class StateSetter:
    def on(self):
        pass
    def off(self):
        pass

class LedStateSetter(StateSetter):
    def on(self):
        print('led on')
    def off(self):
        print('led_off')

class LampStateSetter(StateSetter):
    def on(self):
        print('lamp on')
    def off(self):
        print('lamp off')


class StateGetter:
    def get(self):
        pass

class LedStateGetter(StateGetter):
    def get(self):
        print('current state of led')

class LampStateGetter(StateGetter):
    def get(Self):
        print('current state of lamp')


class LightInteractorFactory:
    def get_state_setter(self) -> StateSetter:
        pass
    def get_state_getter(self) -> StateGetter:
        pass


class LedInteractor(LightInteractorFactory):
    def get_state_setter(self) -> StateSetter:
        return LedStateSetter()

    def get_state_getter(self) -> StateGetter:
        return LedStateGetter()


class LampInteractor(LightInteractorFactory):
    def get_state_setter(self) -> StateGetter:
        return LampStateSetter()

    def get_state_getter(self) -> StateSetter:
        return LampStateGetter()

def read_factory() -> LightInteractorFactory:
    kinds = {
    'led': LedInteractor(),
    'lamp': LampInteractor()
    }

    while True:
        kind = input('What kind?')
        if kind in kinds:
            return kinds[kind]
        print('bad kind')

def main(factory: LightInteractorFactory):
    state_getter = factory.get_state_getter()
    state_setter = factory.get_state_setter()

    #get current state
    state_getter.get()

    #flicker
    state_setter.on()
    state_setter.off()

if __name__=="__main__":
    fac = read_factory()
    main(fac)
