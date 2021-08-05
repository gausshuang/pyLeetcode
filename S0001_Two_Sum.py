import pprint

class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    pprint.pprint( nums )
    pprint.pprint( target )
    d = {}
    for i, num in enumerate( nums ):
      if target - num in d:
        pprint.pprint( d )
        return [ d[ target - num ], i ]
      d[ num ] = i
    # no special case handling because it's assumed that it has only one solution

def main():
    test1 = Solution()
    result = test1.twoSum([100,0,1,2,3,4], 103)
    print(result)

if __name__ == '__main__':
    main()
