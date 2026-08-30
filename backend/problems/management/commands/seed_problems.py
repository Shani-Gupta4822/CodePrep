from django.core.management.base import BaseCommand

from problems.models import Problem


PROBLEMS = [

    # ==================== ARRAYS ====================

    {
        "title": "Two Sum",
        "slug": "two-sum",
        "difficulty": "Easy",
        "topic": "Arrays",
        "description": "Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target.",
        "examples": "Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]",
        "constraints": "2 <= nums.length <= 10^4\nEach input has exactly one solution.",
        "starter_code": "class Solution {\n    public int[] twoSum(int[] nums, int target) {\n        return new int[]{};\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(n)",
        "acceptance": "49.5",

"test_cases": [
    {
        "driver": """
int[] nums = {2, 7, 11, 15};
int target = 9;

Solution solution = new Solution();

int[] result = solution.twoSum(nums, target);

System.out.println(
    java.util.Arrays.toString(result)
);
""",
        "expected": "[0, 1]"
    },

    {
        "driver": """
int[] nums = {3, 2, 4};
int target = 6;

Solution solution = new Solution();

int[] result = solution.twoSum(nums, target);

System.out.println(
    java.util.Arrays.toString(result)
);
""",
        "expected": "[1, 2]"
    }
],
},


    {
        "title": "Best Time to Buy and Sell Stock",
        "slug": "best-time-to-buy-and-sell-stock",
        "difficulty": "Easy",
        "topic": "Arrays",
        "description": "Given an array prices where prices[i] is the price of a stock on day i, find the maximum profit from buying and selling once.",
        "examples": "Input: prices = [7,1,5,3,6,4]\nOutput: 5",
        "constraints": "1 <= prices.length <= 10^5\n0 <= prices[i] <= 10^4",
        "starter_code": "class Solution {\n    public int maxProfit(int[] prices) {\n        return 0;\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(1)",
        "acceptance": "55.0",
        "test_cases": [
    {
        "driver": """
int[] prices = {7, 1, 5, 3, 6, 4};

Solution solution = new Solution();

int result = solution.maxProfit(prices);

System.out.println(result);
""",
        "expected": "5"
    },

    {
        "driver": """
int[] prices = {7, 6, 4, 3, 1};

Solution solution = new Solution();

int result = solution.maxProfit(prices);

System.out.println(result);
""",
        "expected": "0"
    }
],
    },

    {
        "title": "Maximum Subarray",
        "slug": "maximum-subarray",
        "difficulty": "Medium",
        "topic": "Arrays",
        "description": "Given an integer array, find the contiguous subarray with the largest sum.",
        "examples": "Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6",
        "constraints": "1 <= nums.length <= 10^5",
        "starter_code": "class Solution {\n    public int maxSubArray(int[] nums) {\n        return 0;\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(1)",
        "acceptance": "52.0",
        "test_cases": [
    {
        "driver": """
int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};

Solution solution = new Solution();

int result = solution.maxSubArray(nums);

System.out.println(result);
""",
        "expected": "6"
    },
    {
        "driver": """
int[] nums = {1};

Solution solution = new Solution();

int result = solution.maxSubArray(nums);

System.out.println(result);
""",
        "expected": "1"
    }
],
        
    },

    {
        "title": "Contains Duplicate",
        "slug": "contains-duplicate",
        "difficulty": "Easy",
        "topic": "Arrays",
        "description": "Determine whether any value appears at least twice in an integer array.",
        "examples": "Input: nums = [1,2,3,1]\nOutput: true",
        "constraints": "1 <= nums.length <= 10^5",
        "starter_code": "class Solution {\n    public boolean containsDuplicate(int[] nums) {\n        return false;\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(n)",
        "acceptance": "61.0",
        "test_cases": [
    {
        "driver": """
int[] nums = {1, 2, 3, 1};

Solution solution = new Solution();

boolean result = solution.containsDuplicate(nums);

System.out.println(result);
""",
        "expected": "true"
    },
    {
        "driver": """
int[] nums = {1, 2, 3, 4};

Solution solution = new Solution();

boolean result = solution.containsDuplicate(nums);

System.out.println(result);
""",
        "expected": "false"
    }
],
    },

    {
        "title": "Merge Sorted Array",
        "slug": "merge-sorted-array",
        "difficulty": "Easy",
        "topic": "Arrays",
        "description": "Merge two sorted arrays into the first array in sorted order.",
        "examples": "Input: nums1 = [1,2,3,0,0,0], nums2 = [2,5,6]\nOutput: [1,2,2,3,5,6]",
        "constraints": "Arrays are sorted in non-decreasing order.",
        "starter_code": "class Solution {\n    public void merge(int[] nums1, int m, int[] nums2, int n) {\n    }\n}",
        "expected_time": "O(m+n)",
        "expected_space": "O(1)",
        "acceptance": "50.0",
        "test_cases": [
    {
        "driver": """
int[] nums1 = {1, 2, 3, 0, 0, 0};
int[] nums2 = {2, 5, 6};

Solution solution = new Solution();

solution.merge(nums1, 3, nums2, 3);

System.out.println(
    java.util.Arrays.toString(nums1)
);
""",
        "expected": "[1, 2, 2, 3, 5, 6]"
    }
],
    },

    {
        "title": "Product of Array Except Self",
        "slug": "product-of-array-except-self",
        "difficulty": "Medium",
        "topic": "Arrays",
        "description": "Return an array where answer[i] is the product of all elements except nums[i].",
        "examples": "Input: nums = [1,2,3,4]\nOutput: [24,12,8,6]",
        "constraints": "Do not use division.",
        "starter_code": "class Solution {\n    public int[] productExceptSelf(int[] nums) {\n        return new int[]{};\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(1)",
        "acceptance": "66.0",
        "test_cases": [
    {
        "driver": """
int[] nums = {1, 2, 3, 4};

Solution solution = new Solution();

int[] result = solution.productExceptSelf(nums);

System.out.println(
    java.util.Arrays.toString(result)
);
""",
        "expected": "[24, 12, 8, 6]"
    }
],
    },


    # ==================== STRINGS ====================

    {
        "title": "Valid Anagram",
        "slug": "valid-anagram",
        "difficulty": "Easy",
        "topic": "Strings",
        "description": "Determine whether two strings are anagrams of each other.",
        "examples": "Input: s = \"anagram\", t = \"nagaram\"\nOutput: true",
        "constraints": "Strings contain lowercase English letters.",
        "starter_code": "class Solution {\n    public boolean isAnagram(String s, String t) {\n        return false;\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(1)",
        "acceptance": "65.0",
        "test_cases": [
    {
        "driver": """
String s = "anagram";
String t = "nagaram";

Solution solution = new Solution();

boolean result = solution.isAnagram(s, t);

System.out.println(result);
""",
        "expected": "true"
    },
    {
        "driver": """
String s = "rat";
String t = "car";

Solution solution = new Solution();

boolean result = solution.isAnagram(s, t);

System.out.println(result);
""",
        "expected": "false"
    }
],
    },

    {
        "title": "Valid Palindrome",
        "slug": "valid-palindrome",
        "difficulty": "Easy",
        "topic": "Strings",
        "description": "Determine whether a string is a palindrome after converting uppercase letters to lowercase and removing non-alphanumeric characters.",
        "examples": "Input: s = \"A man, a plan, a canal: Panama\"\nOutput: true",
        "constraints": "1 <= s.length <= 2 * 10^5",
        "starter_code": "class Solution {\n    public boolean isPalindrome(String s) {\n        return false;\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(1)",
        "acceptance": "48.0",
        "test_cases": [
    {
        "driver": """
String s = "A man, a plan, a canal: Panama";

Solution solution = new Solution();

boolean result = solution.isPalindrome(s);

System.out.println(result);
""",
        "expected": "true"
    },
    {
        "driver": """
String s = "race a car";

Solution solution = new Solution();

boolean result = solution.isPalindrome(s);

System.out.println(result);
""",
        "expected": "false"
    }
],
    },

    {
        "title": "Longest Substring Without Repeating Characters",
        "slug": "longest-substring-without-repeating-characters",
        "difficulty": "Medium",
        "topic": "Strings",
        "description": "Find the length of the longest substring without repeating characters.",
        "examples": "Input: s = \"abcabcbb\"\nOutput: 3",
        "constraints": "0 <= s.length <= 5 * 10^4",
        "starter_code": "class Solution {\n    public int lengthOfLongestSubstring(String s) {\n        return 0;\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(n)",
        "acceptance": "38.0",
        "test_cases": [
    {
        "driver": """
String s = "abcabcbb";

Solution solution = new Solution();

int result = solution.lengthOfLongestSubstring(s);

System.out.println(result);
""",
        "expected": "3"
    },
    {
        "driver": """
String s = "bbbbb";

Solution solution = new Solution();

int result = solution.lengthOfLongestSubstring(s);

System.out.println(result);
""",
        "expected": "1"
    }
],
    },

    {
        "title": "Longest Common Prefix",
        "slug": "longest-common-prefix",
        "difficulty": "Easy",
        "topic": "Strings",
        "description": "Find the longest common prefix shared by all strings in an array.",
        "examples": "Input: strs = [\"flower\",\"flow\",\"flight\"]\nOutput: \"fl\"",
        "constraints": "1 <= strs.length <= 200",
        "starter_code": "class Solution {\n    public String longestCommonPrefix(String[] strs) {\n        return \"\";\n    }\n}",
        "expected_time": "O(n*m)",
        "expected_space": "O(1)",
        "acceptance": "42.0",
        "test_cases": [
    {
        "driver": """
String[] strs = {"flower", "flow", "flight"};

Solution solution = new Solution();

String result = solution.longestCommonPrefix(strs);

System.out.println(result);
""",
        "expected": "fl"
    }
],
    },

    {
        "title": "Group Anagrams",
        "slug": "group-anagrams",
        "difficulty": "Medium",
        "topic": "Strings",
        "description": "Group strings that are anagrams of each other.",
        "examples": "Input: strs = [\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]\nOutput: [[\"eat\",\"tea\",\"ate\"],[\"tan\",\"nat\"],[\"bat\"]]",
        "constraints": "1 <= strs.length <= 10^4",
        "starter_code": "class Solution {\n    public List<List<String>> groupAnagrams(String[] strs) {\n        return new ArrayList<>();\n    }\n}",
        "expected_time": "O(n*k log k)",
        "expected_space": "O(n*k)",
        "acceptance": "67.0",
        "test_cases": [
    {
        "driver": """
String[] strs = {"eat", "tea", "tan", "ate", "nat", "bat"};

Solution solution = new Solution();

java.util.List<java.util.List<String>> result =
    solution.groupAnagrams(strs);

result.sort((a, b) -> a.toString().compareTo(b.toString()));

for (java.util.List<String> group : result) {
    java.util.Collections.sort(group);
}

System.out.println(result);
""",
        "expected": "[[ate, eat, tea], [bat], [nat, tan]]"
    }
],
    },


    # ==================== BINARY SEARCH ====================

    {
        "title": "Binary Search",
        "slug": "binary-search",
        "difficulty": "Easy",
        "topic": "Binary Search",
        "description": "Given a sorted array and a target value, return the index of the target or -1 if it does not exist.",
        "examples": "Input: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4",
        "constraints": "The array is sorted in ascending order.",
        "starter_code": "class Solution {\n    public int search(int[] nums, int target) {\n        return -1;\n    }\n}",
        "expected_time": "O(log n)",
        "expected_space": "O(1)",
        "acceptance": "59.0",
        "test_cases": [
    {
        "driver": """
int[] nums = {-1, 0, 3, 5, 9, 12};
int target = 9;

Solution solution = new Solution();

int result = solution.search(nums, target);

System.out.println(result);
""",
        "expected": "4"
    },
    {
        "driver": """
int[] nums = {-1, 0, 3, 5, 9, 12};
int target = 2;

Solution solution = new Solution();

int result = solution.search(nums, target);

System.out.println(result);
""",
        "expected": "-1"
    }
],
    },

    {
        "title": "Search Insert Position",
        "slug": "search-insert-position",
        "difficulty": "Easy",
        "topic": "Binary Search",
        "description": "Return the index if target is found, otherwise return the index where it would be inserted.",
        "examples": "Input: nums = [1,3,5,6], target = 5\nOutput: 2",
        "constraints": "The array contains distinct integers.",
        "starter_code": "class Solution {\n    public int searchInsert(int[] nums, int target) {\n        return 0;\n    }\n}",
        "expected_time": "O(log n)",
        "expected_space": "O(1)",
        "acceptance": "45.0",
        "test_cases": [
    {
        "driver": """
int[] nums = {1, 3, 5, 6};
int target = 5;

Solution solution = new Solution();

int result = solution.searchInsert(nums, target);

System.out.println(result);
""",
        "expected": "2"
    },
    {
        "driver": """
int[] nums = {1, 3, 5, 6};
int target = 2;

Solution solution = new Solution();

int result = solution.searchInsert(nums, target);

System.out.println(result);
""",
        "expected": "1"
    }
],

    },

    {
        "title": "Find First and Last Position of Element",
        "slug": "find-first-and-last-position",
        "difficulty": "Medium",
        "topic": "Binary Search",
        "description": "Find the starting and ending position of a target value in a sorted array.",
        "examples": "Input: nums = [5,7,7,8,8,10], target = 8\nOutput: [3,4]",
        "constraints": "The array is sorted in non-decreasing order.",
        "starter_code": "class Solution {\n    public int[] searchRange(int[] nums, int target) {\n        return new int[]{-1,-1};\n    }\n}",
        "expected_time": "O(log n)",
        "expected_space": "O(1)",
        "acceptance": "45.0",
        "test_cases": [
    {
        "driver": """
int[] nums = {5, 7, 7, 8, 8, 10};
int target = 8;

Solution solution = new Solution();

int[] result = solution.searchRange(nums, target);

System.out.println(
    java.util.Arrays.toString(result)
);
""",
        "expected": "[3, 4]"
    },
    {
        "driver": """
int[] nums = {5, 7, 7, 8, 8, 10};
int target = 6;

Solution solution = new Solution();

int[] result = solution.searchRange(nums, target);

System.out.println(
    java.util.Arrays.toString(result)
);
""",
        "expected": "[-1, -1]"
    }
],
    },

    {
        "title": "Search in Rotated Sorted Array",
        "slug": "search-in-rotated-sorted-array",
        "difficulty": "Medium",
        "topic": "Binary Search",
        "description": "Search for a target in a rotated sorted array.",
        "examples": "Input: nums = [4,5,6,7,0,1,2], target = 0\nOutput: 4",
        "constraints": "All values are unique.",
        "starter_code": "class Solution {\n    public int search(int[] nums, int target) {\n        return -1;\n    }\n}",
        "expected_time": "O(log n)",
        "expected_space": "O(1)",
        "acceptance": "42.0",
        "test_cases": [
    {
        "driver": """
int[] nums = {4, 5, 6, 7, 0, 1, 2};
int target = 0;

Solution solution = new Solution();

int result = solution.search(nums, target);

System.out.println(result);
""",
        "expected": "4"
    },
    {
        "driver": """
int[] nums = {4, 5, 6, 7, 0, 1, 2};
int target = 3;

Solution solution = new Solution();

int result = solution.search(nums, target);

System.out.println(result);
""",
        "expected": "-1"
    }
],
    },


    # ==================== LINKED LIST ====================

    {
        "title": "Reverse Linked List",
        "slug": "reverse-linked-list",
        "difficulty": "Easy",
        "topic": "Linked List",
        "description": "Reverse a singly linked list.",
        "examples": "Input: head = [1,2,3,4,5]\nOutput: [5,4,3,2,1]",
        "constraints": "0 <= number of nodes <= 5000",
        "starter_code": "class Solution {\n    public ListNode reverseList(ListNode head) {\n        return null;\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(1)",
        "acceptance": "75.0",
        "test_cases": [
    {
        "driver": """
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
head.next.next.next = new ListNode(4);
head.next.next.next.next = new ListNode(5);

Solution solution = new Solution();

ListNode result = solution.reverseList(head);

while (result != null) {
    System.out.print(result.val);
    if (result.next != null) System.out.print(",");
    result = result.next;
}
System.out.println();
""",
        "expected": "5,4,3,2,1"
    }
],
    },

    {
        "title": "Middle of the Linked List",
        "slug": "middle-of-the-linked-list",
        "difficulty": "Easy",
        "topic": "Linked List",
        "description": "Return the middle node of a singly linked list.",
        "examples": "Input: head = [1,2,3,4,5]\nOutput: [3,4,5]",
        "constraints": "The number of nodes is between 1 and 100.",
        "starter_code": "class Solution {\n    public ListNode middleNode(ListNode head) {\n        return null;\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(1)",
        "acceptance": "80.0",
        "test_cases": [
    {
        "driver": """
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
head.next.next.next = new ListNode(4);
head.next.next.next.next = new ListNode(5);

Solution solution = new Solution();

ListNode result = solution.middleNode(head);

while (result != null) {
    System.out.print(result.val);
    if (result.next != null) System.out.print(",");
    result = result.next;
}
System.out.println();
""",
        "expected": "3,4,5"
    }
],
    },

    {
        "title": "Linked List Cycle",
        "slug": "linked-list-cycle",
        "difficulty": "Easy",
        "topic": "Linked List",
        "description": "Determine whether a linked list contains a cycle.",
        "examples": "Input: head = [3,2,0,-4], pos = 1\nOutput: true",
        "constraints": "The linked list may contain a cycle.",
        "starter_code": "class Solution {\n    public boolean hasCycle(ListNode head) {\n        return false;\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(1)",
        "acceptance": "52.0",
        "test_cases": [
    {
        "driver": """
ListNode head = new ListNode(3);
head.next = new ListNode(2);
head.next.next = new ListNode(0);
head.next.next.next = new ListNode(-4);

head.next.next.next.next = head.next;

Solution solution = new Solution();

boolean result = solution.hasCycle(head);

System.out.println(result);
""",
        "expected": "true"
    },
    {
        "driver": """
ListNode head = new ListNode(1);
head.next = new ListNode(2);

Solution solution = new Solution();

boolean result = solution.hasCycle(head);

System.out.println(result);
""",
        "expected": "false"
    }
],
    },

    {
        "title": "Merge Two Sorted Lists",
        "slug": "merge-two-sorted-lists",
        "difficulty": "Easy",
        "topic": "Linked List",
        "description": "Merge two sorted linked lists into one sorted linked list.",
        "examples": "Input: list1 = [1,2,4], list2 = [1,3,4]\nOutput: [1,1,2,3,4,4]",
        "constraints": "Both linked lists are sorted.",
        "starter_code": "class Solution {\n    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {\n        return null;\n    }\n}",
        "expected_time": "O(n+m)",
        "expected_space": "O(1)",
        "acceptance": "65.0",
        "test_cases": [
    {
        "driver": """
ListNode list1 = new ListNode(1);
list1.next = new ListNode(2);
list1.next.next = new ListNode(4);

ListNode list2 = new ListNode(1);
list2.next = new ListNode(3);
list2.next.next = new ListNode(4);

Solution solution = new Solution();

ListNode result = solution.mergeTwoLists(list1, list2);

while (result != null) {
    System.out.print(result.val);
    if (result.next != null) System.out.print(",");
    result = result.next;
}
System.out.println();
""",
        "expected": "1,1,2,3,4,4"
    }
],
    },


    # ==================== STACK & QUEUE ====================

    {
        "title": "Valid Parentheses",
        "slug": "valid-parentheses",
        "difficulty": "Easy",
        "topic": "Stack",
        "description": "Determine whether a string containing brackets is valid.",
        "examples": "Input: s = \"()[]{}\"\nOutput: true",
        "constraints": "1 <= s.length <= 10^4",
        "starter_code": "class Solution {\n    public boolean isValid(String s) {\n        return false;\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(n)",
        "acceptance": "42.0",
        "test_cases": [
    {
        "driver": """
String s = "()[]{}";

Solution solution = new Solution();

boolean result = solution.isValid(s);

System.out.println(result);
""",
        "expected": "true"
    },
    {
        "driver": """
String s = "(]";

Solution solution = new Solution();

boolean result = solution.isValid(s);

System.out.println(result);
""",
        "expected": "false"
    }
],
    },

    {
        "title": "Min Stack",
        "slug": "min-stack",
        "difficulty": "Medium",
        "topic": "Stack",
        "description": "Design a stack that supports push, pop, top and retrieving the minimum element in constant time.",
        "examples": "Operations: push(-2), push(0), push(-3), getMin()\nOutput: -3",
        "constraints": "All operations should run in O(1).",
        "starter_code": "class MinStack {\n    public MinStack() {\n    }\n\n    public void push(int val) {\n    }\n\n    public void pop() {\n    }\n\n    public int top() {\n        return 0;\n    }\n\n    public int getMin() {\n        return 0;\n    }\n}",
        "expected_time": "O(1)",
        "expected_space": "O(n)",
        "acceptance": "56.0",
    },

    {
        "title": "Implement Queue using Stacks",
        "slug": "implement-queue-using-stacks",
        "difficulty": "Easy",
        "topic": "Queue",
        "description": "Implement a first-in-first-out queue using only stacks.",
        "examples": "push(1), push(2), peek() -> 1",
        "constraints": "Standard queue operations should be supported.",
        "starter_code": "class MyQueue {\n    public MyQueue() {\n    }\n\n    public void push(int x) {\n    }\n\n    public int pop() {\n        return 0;\n    }\n\n    public int peek() {\n        return 0;\n    }\n\n    public boolean empty() {\n        return false;\n    }\n}",
        "expected_time": "O(1) amortized",
        "expected_space": "O(n)",
        "acceptance": "70.0",
    },

    {
        "title": "Daily Temperatures",
        "slug": "daily-temperatures",
        "difficulty": "Medium",
        "topic": "Stack",
        "description": "Return the number of days until a warmer temperature for each day.",
        "examples": "Input: temperatures = [73,74,75,71,69,72,76,73]\nOutput: [1,1,4,2,1,1,0,0]",
        "constraints": "1 <= temperatures.length <= 10^5",
        "starter_code": "class Solution {\n    public int[] dailyTemperatures(int[] temperatures) {\n        return new int[]{};\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(n)",
        "acceptance": "66.0",
        "test_cases": [
    {
        "driver": """
int[] temperatures = {73, 74, 75, 71, 69, 72, 76, 73};

Solution solution = new Solution();

int[] result = solution.dailyTemperatures(temperatures);

System.out.println(
    java.util.Arrays.toString(result)
);
""",
        "expected": "[1, 1, 4, 2, 1, 1, 0, 0]"
    }
],
    },


    # ==================== TREES ====================

    {
        "title": "Maximum Depth of Binary Tree",
        "slug": "maximum-depth-of-binary-tree",
        "difficulty": "Easy",
        "topic": "Trees",
        "description": "Return the maximum depth of a binary tree.",
        "examples": "Input: root = [3,9,20,null,null,15,7]\nOutput: 3",
        "constraints": "Number of nodes is between 0 and 10^4.",
        "starter_code": "class Solution {\n    public int maxDepth(TreeNode root) {\n        return 0;\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(h)",
        "acceptance": "75.0",
        "test_cases": [
    {
        "driver": """
TreeNode root = new TreeNode(3);
root.left = new TreeNode(9);
root.right = new TreeNode(20);
root.right.left = new TreeNode(15);
root.right.right = new TreeNode(7);

Solution solution = new Solution();

int result = solution.maxDepth(root);

System.out.println(result);
""",
        "expected": "3"
    }
],
    },

    {
        "title": "Invert Binary Tree",
        "slug": "invert-binary-tree",
        "difficulty": "Easy",
        "topic": "Trees",
        "description": "Invert a binary tree by swapping every left and right child.",
        "examples": "Input: root = [4,2,7,1,3,6,9]\nOutput: [4,7,2,9,6,3,1]",
        "constraints": "0 <= nodes <= 100.",
        "starter_code": "class Solution {\n    public TreeNode invertTree(TreeNode root) {\n        return null;\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(h)",
        "acceptance": "77.0",
        "test_cases": [
    {
        "driver": """
TreeNode root = new TreeNode(4);
root.left = new TreeNode(2);
root.right = new TreeNode(7);
root.left.left = new TreeNode(1);
root.left.right = new TreeNode(3);
root.right.left = new TreeNode(6);
root.right.right = new TreeNode(9);

Solution solution = new Solution();

TreeNode result = solution.invertTree(root);

System.out.println(
    result.val + "," +
    result.left.val + "," +
    result.right.val
);
""",
        "expected": "4,7,2"
    }
],
    },

    {
        "title": "Binary Tree Level Order Traversal",
        "slug": "binary-tree-level-order-traversal",
        "difficulty": "Medium",
        "topic": "Trees",
        "description": "Return the level order traversal of a binary tree.",
        "examples": "Input: root = [3,9,20,null,null,15,7]\nOutput: [[3],[9,20],[15,7]]",
        "constraints": "The tree may be empty.",
        "starter_code": "class Solution {\n    public List<List<Integer>> levelOrder(TreeNode root) {\n        return new ArrayList<>();\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(n)",
        "acceptance": "70.0",
        "test_cases": [
    {
        "driver": """
TreeNode root = new TreeNode(3);
root.left = new TreeNode(9);
root.right = new TreeNode(20);
root.right.left = new TreeNode(15);
root.right.right = new TreeNode(7);

Solution solution = new Solution();

java.util.List<java.util.List<Integer>> result =
    solution.levelOrder(root);

System.out.println(result);
""",
        "expected": "[[3], [9, 20], [15, 7]]"
    }
],
    },

    {
        "title": "Validate Binary Search Tree",
        "slug": "validate-binary-search-tree",
        "difficulty": "Medium",
        "topic": "Trees",
        "description": "Determine whether a binary tree is a valid binary search tree.",
        "examples": "Input: root = [2,1,3]\nOutput: true",
        "constraints": "Tree values are integers.",
        "starter_code": "class Solution {\n    public boolean isValidBST(TreeNode root) {\n        return false;\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(h)",
        "acceptance": "35.0",
        "test_cases": [
    {
        "driver": """
TreeNode root = new TreeNode(2);
root.left = new TreeNode(1);
root.right = new TreeNode(3);

Solution solution = new Solution();

boolean result = solution.isValidBST(root);

System.out.println(result);
""",
        "expected": "true"
    },
    {
        "driver": """
TreeNode root = new TreeNode(5);
root.left = new TreeNode(1);
root.right = new TreeNode(4);
root.right.left = new TreeNode(3);
root.right.right = new TreeNode(6);

Solution solution = new Solution();

boolean result = solution.isValidBST(root);

System.out.println(result);
""",
        "expected": "false"
    }
],
    },

    {
        "title": "Lowest Common Ancestor of a BST",
        "slug": "lowest-common-ancestor-bst",
        "difficulty": "Medium",
        "topic": "Trees",
        "description": "Find the lowest common ancestor of two nodes in a binary search tree.",
        "examples": "Input: root = [6,2,8,0,4,7,9], p = 2, q = 8\nOutput: 6",
        "constraints": "p and q exist in the tree.",
        "starter_code": "class Solution {\n    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {\n        return null;\n    }\n}",
        "expected_time": "O(h)",
        "expected_space": "O(1)",
        "acceptance": "65.0",
        "test_cases": [
    {
        "driver": """
TreeNode root = new TreeNode(6);
root.left = new TreeNode(2);
root.right = new TreeNode(8);
root.left.left = new TreeNode(0);
root.left.right = new TreeNode(4);
root.right.left = new TreeNode(7);
root.right.right = new TreeNode(9);

TreeNode p = root.left;
TreeNode q = root.right;

Solution solution = new Solution();

TreeNode result =
    solution.lowestCommonAncestor(root, p, q);

System.out.println(result.val);
""",
        "expected": "6"
    }
],
        
    },


    # ==================== GRAPH ====================

    {
        "title": "Number of Islands",
        "slug": "number-of-islands",
        "difficulty": "Medium",
        "topic": "Graph",
        "description": "Count the number of islands in a 2D grid.",
        "examples": "Input: grid = [[1,1,0],[1,0,0],[0,0,1]]\nOutput: 2",
        "constraints": "Grid contains '1' and '0'.",
        "starter_code": "class Solution {\n    public int numIslands(char[][] grid) {\n        return 0;\n    }\n}",
        "expected_time": "O(m*n)",
        "expected_space": "O(m*n)",
        "acceptance": "60.0",
        "test_cases": [
    {
        "driver": """
char[][] grid = {
    {'1','1','0'},
    {'1','0','0'},
    {'0','0','1'}
};

Solution solution = new Solution();

int result = solution.numIslands(grid);

System.out.println(result);
""",
        "expected": "2"
    }
],
    },

    {
        "title": "Flood Fill",
        "slug": "flood-fill",
        "difficulty": "Easy",
        "topic": "Graph",
        "description": "Perform a flood fill operation on an image starting from a given pixel.",
        "examples": "Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2",
        "constraints": "Image dimensions are valid.",
        "starter_code": "class Solution {\n    public int[][] floodFill(int[][] image, int sr, int sc, int color) {\n        return image;\n    }\n}",
        "expected_time": "O(m*n)",
        "expected_space": "O(m*n)",
        "acceptance": "70.0",
        "test_cases": [
    {
        "driver": """
int[][] image = {
    {1,1,1},
    {1,1,0},
    {1,0,1}
};

Solution solution = new Solution();

int[][] result =
    solution.floodFill(image, 1, 1, 2);

System.out.println(
    java.util.Arrays.deepToString(result)
);
""",
        "expected": "[[2, 2, 2], [2, 2, 0], [2, 0, 1]]"
    }
],
    },

    {
        "title": "Clone Graph",
        "slug": "clone-graph",
        "difficulty": "Medium",
        "topic": "Graph",
        "description": "Return a deep copy of an undirected connected graph.",
        "examples": "Input: adjacencyList = [[2,4],[1,3],[2,4],[1,3]]",
        "constraints": "Graph contains no self-loops.",
        "starter_code": "class Solution {\n    public Node cloneGraph(Node node) {\n        return null;\n    }\n}",
        "expected_time": "O(V+E)",
        "expected_space": "O(V)",
        "acceptance": "55.0",

    },

    {
        "title": "Course Schedule",
        "slug": "course-schedule",
        "difficulty": "Medium",
        "topic": "Graph",
        "description": "Determine whether all courses can be finished given prerequisite relationships.",
        "examples": "Input: numCourses = 2, prerequisites = [[1,0]]\nOutput: true",
        "constraints": "Prerequisites form a directed graph.",
        "starter_code": "class Solution {\n    public boolean canFinish(int numCourses, int[][] prerequisites) {\n        return false;\n    }\n}",
        "expected_time": "O(V+E)",
        "expected_space": "O(V+E)",
        "acceptance": "48.0",
        "test_cases": [
    {
        "driver": """
int numCourses = 2;

int[][] prerequisites = {
    {1, 0}
};

Solution solution = new Solution();

boolean result =
    solution.canFinish(numCourses, prerequisites);

System.out.println(result);
""",
        "expected": "true"
    },
    {
        "driver": """
int numCourses = 2;

int[][] prerequisites = {
    {1, 0},
    {0, 1}
};

Solution solution = new Solution();

boolean result =
    solution.canFinish(numCourses, prerequisites);

System.out.println(result);
""",
        "expected": "false"
    }
],
    },


    # ==================== DYNAMIC PROGRAMMING ====================

    {
        "title": "Climbing Stairs",
        "slug": "climbing-stairs",
        "difficulty": "Easy",
        "topic": "Dynamic Programming",
        "description": "Count the number of distinct ways to climb n stairs when you can climb one or two steps at a time.",
        "examples": "Input: n = 3\nOutput: 3",
        "constraints": "1 <= n <= 45",
        "starter_code": "class Solution {\n    public int climbStairs(int n) {\n        return 0;\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(1)",
        "acceptance": "52.0",
        "test_cases": [
    {
        "driver": """
int n = 3;

Solution solution = new Solution();

int result = solution.climbStairs(n);

System.out.println(result);
""",
        "expected": "3"
    },
    {
        "driver": """
int n = 5;

Solution solution = new Solution();

int result = solution.climbStairs(n);

System.out.println(result);
""",
        "expected": "8"
    }
],
    },

    {
        "title": "House Robber",
        "slug": "house-robber",
        "difficulty": "Medium",
        "topic": "Dynamic Programming",
        "description": "Determine the maximum amount of money that can be robbed without robbing adjacent houses.",
        "examples": "Input: nums = [2,7,9,3,1]\nOutput: 12",
        "constraints": "1 <= nums.length <= 100",
        "starter_code": "class Solution {\n    public int rob(int[] nums) {\n        return 0;\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(1)",
        "acceptance": "50.0",
        "test_cases": [
    {
        "driver": """
int[] nums = {2, 7, 9, 3, 1};

Solution solution = new Solution();

int result = solution.rob(nums);

System.out.println(result);
""",
        "expected": "12"
    },
    {
        "driver": """
int[] nums = {2, 1, 1, 2};

Solution solution = new Solution();

int result = solution.rob(nums);

System.out.println(result);
""",
        "expected": "4"
    }
],
    },

    {
        "title": "Coin Change",
        "slug": "coin-change",
        "difficulty": "Medium",
        "topic": "Dynamic Programming",
        "description": "Return the fewest number of coins needed to make a given amount.",
        "examples": "Input: coins = [1,2,5], amount = 11\nOutput: 3",
        "constraints": "1 <= coins.length <= 12\n0 <= amount <= 10^4",
        "starter_code": "class Solution {\n    public int coinChange(int[] coins, int amount) {\n        return -1;\n    }\n}",
        "expected_time": "O(amount*n)",
        "expected_space": "O(amount)",
        "acceptance": "45.0",
        "test_cases": [
    {
        "driver": """
int[] coins = {1, 2, 5};
int amount = 11;

Solution solution = new Solution();

int result = solution.coinChange(coins, amount);

System.out.println(result);
""",
        "expected": "3"
    },
    {
        "driver": """
int[] coins = {2};
int amount = 3;

Solution solution = new Solution();

int result = solution.coinChange(coins, amount);

System.out.println(result);
""",
        "expected": "-1"
    }
],
    },

    {
        "title": "Longest Increasing Subsequence",
        "slug": "longest-increasing-subsequence",
        "difficulty": "Medium",
        "topic": "Dynamic Programming",
        "description": "Find the length of the longest strictly increasing subsequence.",
        "examples": "Input: nums = [10,9,2,5,3,7,101,18]\nOutput: 4",
        "constraints": "1 <= nums.length <= 2500",
        "starter_code": "class Solution {\n    public int lengthOfLIS(int[] nums) {\n        return 0;\n    }\n}",
        "expected_time": "O(n log n)",
        "expected_space": "O(n)",
        "acceptance": "58.0",
        "test_cases": [
    {
        "driver": """
int[] nums = {10, 9, 2, 5, 3, 7, 101, 18};

Solution solution = new Solution();

int result = solution.lengthOfLIS(nums);

System.out.println(result);
""",
        "expected": "4"
    },
    {
        "driver": """
int[] nums = {0, 1, 0, 3, 2, 3};

Solution solution = new Solution();

int result = solution.lengthOfLIS(nums);

System.out.println(result);
""",
        "expected": "4"
    }
],
    },

    {
        "title": "Longest Common Subsequence",
        "slug": "longest-common-subsequence",
        "difficulty": "Medium",
        "topic": "Dynamic Programming",
        "description": "Find the length of the longest common subsequence between two strings.",
        "examples": "Input: text1 = \"abcde\", text2 = \"ace\"\nOutput: 3",
        "constraints": "1 <= text1.length, text2.length <= 1000",
        "starter_code": "class Solution {\n    public int longestCommonSubsequence(String text1, String text2) {\n        return 0;\n    }\n}",
        "expected_time": "O(n*m)",
        "expected_space": "O(n*m)",
        "acceptance": "58.0",
        "test_cases": [
    {
        "driver": """
String text1 = "abcde";
String text2 = "ace";

Solution solution = new Solution();

int result =
    solution.longestCommonSubsequence(text1, text2);

System.out.println(result);
""",
        "expected": "3"
    },
    {
        "driver": """
String text1 = "abc";
String text2 = "abc";

Solution solution = new Solution();

int result =
    solution.longestCommonSubsequence(text1, text2);

System.out.println(result);
""",
        "expected": "3"
    }
],
    },

    # ==================== EXTRA INTERVIEW PROBLEMS ====================

    {
        "title": "Merge Intervals",
        "slug": "merge-intervals",
        "difficulty": "Medium",
        "topic": "Arrays",
        "description": "Merge all overlapping intervals.",
        "examples": "Input: intervals = [[1,3],[2,6],[8,10],[15,18]]\nOutput: [[1,6],[8,10],[15,18]]",
        "constraints": "Intervals may overlap.",
        "starter_code": "class Solution {\n    public int[][] merge(int[][] intervals) {\n        return new int[][]{};\n    }\n}",
        "expected_time": "O(n log n)",
        "expected_space": "O(n)",
        "acceptance": "49.0",
        "test_cases": [
    {
        "driver": """
int[][] intervals = {
    {1, 3},
    {2, 6},
    {8, 10},
    {15, 18}
};

Solution solution = new Solution();

int[][] result = solution.merge(intervals);

System.out.println(
    java.util.Arrays.deepToString(result)
);
""",
        "expected": "[[1, 6], [8, 10], [15, 18]]"
    }
],
    },

    {
        "title": "Subarray Sum Equals K",
        "slug": "subarray-sum-equals-k",
        "difficulty": "Medium",
        "topic": "Arrays",
        "description": "Count the number of continuous subarrays whose sum equals k.",
        "examples": "Input: nums = [1,1,1], k = 2\nOutput: 2",
        "constraints": "1 <= nums.length <= 2 * 10^4",
        "starter_code": "class Solution {\n    public int subarraySum(int[] nums, int k) {\n        return 0;\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(n)",
        "acceptance": "45.0",
        "test_cases": [
    {
        "driver": """
int[] nums = {1, 1, 1};
int k = 2;

Solution solution = new Solution();

int result = solution.subarraySum(nums, k);

System.out.println(result);
""",
        "expected": "2"
    },
    {
        "driver": """
int[] nums = {1, 2, 3};
int k = 3;

Solution solution = new Solution();

int result = solution.subarraySum(nums, k);

System.out.println(result);
""",
        "expected": "2"
    }
],
    },

    {
        "title": "Kth Largest Element in an Array",
        "slug": "kth-largest-element",
        "difficulty": "Medium",
        "topic": "Arrays",
        "description": "Find the kth largest element in an unsorted array.",
        "examples": "Input: nums = [3,2,1,5,6,4], k = 2\nOutput: 5",
        "constraints": "1 <= k <= nums.length",
        "starter_code": "class Solution {\n    public int findKthLargest(int[] nums, int k) {\n        return 0;\n    }\n}",
        "expected_time": "O(n log n)",
        "expected_space": "O(n)",
        "acceptance": "68.0",
        "test_cases": [
    {
        "driver": """
int[] nums = {3, 2, 1, 5, 6, 4};
int k = 2;

Solution solution = new Solution();

int result = solution.findKthLargest(nums, k);

System.out.println(result);
""",
        "expected": "5"
    },
    {
        "driver": """
int[] nums = {3, 2, 3, 1, 2, 4, 5, 5, 6};
int k = 4;

Solution solution = new Solution();

int result = solution.findKthLargest(nums, k);

System.out.println(result);
""",
        "expected": "4"
    }
],
    },

    {
        "title": "Word Break",
        "slug": "word-break",
        "difficulty": "Medium",
        "topic": "Dynamic Programming",
        "description": "Determine whether a string can be segmented into a sequence of dictionary words.",
        "examples": "Input: s = \"leetcode\", wordDict = [\"leet\",\"code\"]\nOutput: true",
        "constraints": "1 <= s.length <= 300",
        "starter_code": "class Solution {\n    public boolean wordBreak(String s, List<String> wordDict) {\n        return false;\n    }\n}",
        "expected_time": "O(n^2)",
        "expected_space": "O(n)",
        "acceptance": "47.0",
        "test_cases": [
    {
        "driver": """
String s = "leetcode";

java.util.List<String> wordDict =
    java.util.Arrays.asList("leet", "code");

Solution solution = new Solution();

boolean result = solution.wordBreak(s, wordDict);

System.out.println(result);
""",
        "expected": "true"
    },
    {
        "driver": """
String s = "catsandog";

java.util.List<String> wordDict =
    java.util.Arrays.asList(
        "cats", "dog", "sand", "and", "cat"
    );

Solution solution = new Solution();

boolean result = solution.wordBreak(s, wordDict);

System.out.println(result);
""",
        "expected": "false"
    }
],
    },

    {
        "title": "Maximum Product Subarray",
        "slug": "maximum-product-subarray",
        "difficulty": "Medium",
        "topic": "Dynamic Programming",
        "description": "Find the contiguous subarray with the largest product.",
        "examples": "Input: nums = [2,3,-2,4]\nOutput: 6",
        "constraints": "1 <= nums.length <= 2 * 10^4",
        "starter_code": "class Solution {\n    public int maxProduct(int[] nums) {\n        return 0;\n    }\n}",
        "expected_time": "O(n)",
        "expected_space": "O(1)",
        "acceptance": "35.0",
        "test_cases": [
    {
        "driver": """
int[] nums = {2, 3, -2, 4};

Solution solution = new Solution();

int result = solution.maxProduct(nums);

System.out.println(result);
""",
        "expected": "6"
    },
    {
        "driver": """
int[] nums = {-2, 0, -1};

Solution solution = new Solution();

int result = solution.maxProduct(nums);

System.out.println(result);
""",
        "expected": "0"
    }
],
    },
]


class Command(BaseCommand):

    help = "Seed CodePrep with DSA problems"

    def handle(self, *args, **kwargs):

        created = 0
        updated = 0

        for data in PROBLEMS:

            slug = data["slug"]

            problem, was_created = Problem.objects.update_or_create(
                slug=slug,
                defaults=data,
            )

            if was_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded {len(PROBLEMS)} problems. "
                f"Created: {created}, Updated: {updated}"
            )
        )