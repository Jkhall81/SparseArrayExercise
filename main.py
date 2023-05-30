class SparseArray:
	def __init__(self, default_value, values=None):
		self.default_value = default_value
		self.sparse_dict = {}
		if values is not None:
			for index, value in enumerate(values):
				if value != default_value:
					self.sparse_dict[index] = value

	def __getitem__(self, index):
		return self.sparse_dict.get(index, self.default_value)

	def __setitem__(self, index, value):
		if value == self.default_value:
			self.sparse_dict.pop(index, None)
		else:
			self.sparse_dict[index] = value

	def __delitem__(self, index):
		self.sparse_dict.pop(index, None)

	def __len__(self):
		return len(self.sparse_dict)

	def __str__(self):
		return str([self[i] for i in range(len(self))])
