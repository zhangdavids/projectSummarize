class Borg(object):
	"""
	任何时候都共享相同的状态的事实，克服琐碎单例实现问题的方案
	"""
	_state = {}

	def __new__(self, *args, **kwargs):
		ob = super().__new__(cls, *args, **kwargs)
		ob.__dict__ = cls._state
		return ob



class Singleton(type):
	_instance = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instance:
			cls._instance[cls] = super().__call__(*args, **kwargs)

		return cls._instance[cls]
