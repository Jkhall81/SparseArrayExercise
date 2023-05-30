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
		highest_key = max(self.sparse_dict.keys())
		return highest_key + 1

	def __str__(self):
		return str([self[i] for i in range(len(self))])

	def __contains__(self, value):
		return value in self.sparse_dict

	def check_index_range(self, index):
		if index >= len(self.sparse_dict):
			raise IndexError("Index is out of range!!")

	def add_value(self, value):
		index = len(self.sparse_dict)
		self.sparse_dict[index] = value
