import { useEffect,useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import Editor from "@monaco-editor/react";

import {
  ArrowLeft,
  Play,
  Send,
  Bot,
  CheckCircle2,
  Clock3,
  Database,
  ChevronDown,
} from "lucide-react";

import "./ProblemDetail.css";


const problemData = {

  1: {
    title: "Two Sum",
    difficulty: "Easy",
    topic: "Array",
    acceptance: "49.2%",

    description:
      "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",

    examples: [
      {
        input: "nums = [2,7,11,15], target = 9",
        output: "[0,1]",
        explanation:
          "Because nums[0] + nums[1] == 9.",
      },
      {
        input: "nums = [3,2,4], target = 6",
        output: "[1,2]",
        explanation:
          "Because nums[1] + nums[2] == 6.",
      },
    ],

    constraints: [
      "2 <= nums.length <= 10⁴",
      "-10⁹ <= nums[i] <= 10⁹",
      "-10⁹ <= target <= 10⁹",
      "Only one valid answer exists.",
    ],

    starterCode:
`class Solution {
    public int[] twoSum(int[] nums, int target) {
        
    }
}`,
  },


  2: {
    title: "Valid Parentheses",
    difficulty: "Easy",
    topic: "Stack",
    acceptance: "41.5%",

    description:
      "Given a string containing brackets, determine whether the input string has valid matching and properly ordered brackets.",

    examples: [
      {
        input: 's = "()"',
        output: "true",
        explanation:
          "The opening and closing parentheses match.",
      },
      {
        input: 's = "()[]{}"',
        output: "true",
        explanation:
          "All brackets are correctly matched.",
      },
    ],

    constraints: [
      "1 <= s.length <= 10⁴",
      "s consists of parentheses only.",
    ],

    starterCode:
`class Solution {
    public boolean isValid(String s) {
        
    }
}`,
  },


  3: {
    title: "Binary Search",
    difficulty: "Easy",
    topic: "Binary Search",
    acceptance: "57.1%",

    description:
      "Given a sorted array of integers nums and an integer target, return the index of target if it exists. Otherwise, return -1.",

    examples: [
      {
        input: "nums = [-1,0,3,5,9,12], target = 9",
        output: "4",
        explanation:
          "9 exists in nums and its index is 4.",
      },
      {
        input: "nums = [-1,0,3,5,9,12], target = 2",
        output: "-1",
        explanation:
          "2 does not exist in the array.",
      },
    ],

    constraints: [
      "1 <= nums.length <= 10⁴",
      "-10⁴ < nums[i], target < 10⁴",
      "All integers in nums are unique.",
      "nums is sorted in ascending order.",
    ],

    starterCode:
`class Solution {
    public int search(int[] nums, int target) {
        
    }
}`,
  },


  4: {
    title:
      "Longest Substring Without Repeating Characters",

    difficulty: "Medium",

    topic: "Sliding Window",

    acceptance: "36.4%",

    description:
      "Given a string s, find the length of the longest substring without repeating characters.",

    examples: [
      {
        input: 's = "abcabcbb"',
        output: "3",
        explanation:
          'The answer is "abc", with length 3.',
      },
      {
        input: 's = "bbbbb"',
        output: "1",
        explanation:
          'The answer is "b", with length 1.',
      },
    ],

    constraints: [
      "0 <= s.length <= 5 * 10⁴",
      "s consists of English letters, digits, symbols and spaces.",
    ],

    starterCode:
`class Solution {
    public int lengthOfLongestSubstring(String s) {
        
    }
}`,
  },


  5: {
    title: "Container With Most Water",

    difficulty: "Medium",

    topic: "Two Pointers",

    acceptance: "56.8%",

    description:
      "Given an integer array height, find two lines that together with the x-axis form a container containing the most water.",

    examples: [
      {
        input: "height = [1,8,6,2,5,4,8,3,7]",
        output: "49",
        explanation:
          "The maximum container area is 49.",
      },
    ],

    constraints: [
      "2 <= height.length <= 10⁵",
      "0 <= height[i] <= 10⁴",
    ],

    starterCode:
`class Solution {
    public int maxArea(int[] height) {
        
    }
}`,
  },


  6: {
    title: "3Sum",

    difficulty: "Medium",

    topic: "Sorting",

    acceptance: "35.0%",

    description:
      "Given an integer array nums, return all unique triplets that sum to zero.",

    examples: [
      {
        input: "nums = [-1,0,1,2,-1,-4]",
        output: "[[-1,-1,2],[-1,0,1]]",
        explanation:
          "These are the unique triplets whose sum is zero.",
      },
    ],

    constraints: [
      "3 <= nums.length <= 3000",
      "-10⁵ <= nums[i] <= 10⁵",
    ],

    starterCode:
`class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
    }
}`,
  },


  7: {
    title: "Merge k Sorted Lists",

    difficulty: "Hard",

    topic: "Linked List",

    acceptance: "52.4%",

    description:
      "Merge k sorted linked lists and return it as one sorted linked list.",

    examples: [
      {
        input: "lists = [[1,4,5],[1,3,4],[2,6]]",
        output: "[1,1,2,3,4,4,5,6]",
        explanation:
          "All lists are merged into one sorted list.",
      },
    ],

    constraints: [
      "k == lists.length",
      "0 <= k <= 10⁴",
      "0 <= lists[i].length <= 500",
    ],

    starterCode:
`class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        
    }
}`,
  },


  8: {
    title: "Word Ladder",

    difficulty: "Hard",

    topic: "Graph",

    acceptance: "39.0%",

    description:
      "Return the number of words in the shortest transformation sequence from beginWord to endWord.",

    examples: [
      {
        input:
          'beginWord = "hit", endWord = "cog"',
        output: "5",
        explanation:
          "One shortest transformation is hit → hot → dot → dog → cog.",
      },
    ],

    constraints: [
      "1 <= beginWord.length <= 10",
      "endWord.length == beginWord.length",
      "All words have the same length.",
    ],

    starterCode:
`class Solution {
    public int ladderLength(
        String beginWord,
        String endWord,
        List<String> wordList
    ) {
        
    }
}`,
  },
};


function ProblemDetail() {

  const { id } = useParams();

  const navigate = useNavigate();

  const [problem, setProblem] = useState(null);


  const [language, setLanguage] =
    useState("Java");


  const [code, setCode] = useState("");
const [runResult, setRunResult] = useState(null);
const [running, setRunning] = useState(false);

useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}/api/problems/${id}/`)
      .then((response) => response.json())
      .then((data) => {
  console.log("PROBLEM API:", data);

  setProblem({
    ...data,

    examples: Array.isArray(data.examples)
      ? data.examples
      : [],

    constraints: Array.isArray(data.constraints)
      ? data.constraints
      : [],
  });

  setCode(data.starter_code || "");
})
      .catch((error) => {
        console.error("Problem fetch error:", error);
      });
  }, [id]);


 
  const handleRun = async () => {
  setRunning(true);
  setRunResult(null);

  try {

    const response = await fetch(
      `${import.meta.env.VITE_API_URL}/api/problems/run/`,
      {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
  code: code,
  problem_id: Number(id),
}),
      }
    );

    const data = await response.json();

    setRunResult(data);

  } catch (error) {

    console.error(error);

    setRunResult({
      status: "Error",
      output: "Unable to run code.",
    });

  } finally {

    setRunning(false);

  }

};

const handleSubmit = async () => {
    


  if (!code.trim()) {
    setRunResult({
      status: "Error",
      output: "Please write some code first.",
    });
    return;
  }

  try {

    const response = await fetch(
      `${import.meta.env.VITE_API_URL}/api/problems/submit/`,
      {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          code: code,
          problem_id: Number(id),
        }),
      }
    );

    const data = await response.json();
    console.log("SUBMIT RESPONSE:", data);

    setRunResult({
      status: data.status,
      output: data.message || data.error || "",
    });

  } catch (error) {

    console.error(error);

    setRunResult({
      status: "Error",
      output: "Unable to submit code.",
    });

  }

};
if (!problem) {
  return <div>Loading...</div>;
}

  return (

    <div className="problem-detail">


      {/* =========================
          TOP BAR
      ========================== */}

      <div className="problem-topbar">

        <button
          className="back-button"
          onClick={() => navigate("/problems")}
        >

          <ArrowLeft size={16} />

          Problems

        </button>


        <div className="problem-top-title">

          <span>
            Problem #{id}
          </span>

          <strong>
            {problem.title}
          </strong>

        </div>


        <button
          className="ai-help-button"
          onClick={() => navigate("/assistant")}
        >

          <Bot size={15} />

          Ask AI

        </button>

      </div>


      {/* =========================
          MAIN
      ========================== */}

      <div className="problem-workspace">


        {/* =========================
            LEFT
        ========================== */}

        <section className="problem-description">


          <div className="problem-title-row">

            <h1>
              {problem.title}
            </h1>


            <span
              className={
                `difficulty-badge ${problem.difficulty.toLowerCase()}`
              }
            >
              {problem.difficulty}
            </span>

          </div>


          <div className="problem-meta">

            <span>
              {problem.topic}
            </span>

            <span>
              Acceptance {problem.acceptance}
            </span>

          </div>


          <div className="description-section">

            <h2>
              Description
            </h2>

            <p>
              {problem.description}
            </p>

          </div>


          {/* EXAMPLES */}

          <div className="description-section">

            <h2>
              Examples
            </h2>


            {problem.examples.map(
              (example, index) => (

                <div
                  className="example-box"
                  key={index}
                >

                  <strong>
                    Example {index + 1}
                  </strong>


                  <div className="example-code">

                    <div>
                      <span>Input</span>

                      <code>
                        {example.input}
                      </code>
                    </div>


                    <div>
                      <span>Output</span>

                      <code>
                        {example.output}
                      </code>
                    </div>

                  </div>


                  <p>
                    {example.explanation}
                  </p>

                </div>

              )
            )}

          </div>


          {/* CONSTRAINTS */}

          <div className="description-section">

            <h2>
              Constraints
            </h2>


            <ul>

              {problem.constraints.map(
                (constraint, index) => (

                  <li key={index}>
                    <code>
                      {constraint}
                    </code>
                  </li>

                )
              )}

            </ul>

          </div>


          {/* COMPLEXITY */}

          <div className="complexity-box">

            <div>

              <Clock3 size={15} />

              <span>
                Expected Time
              </span>

              <strong>
                O(log n)
              </strong>

            </div>


            <div>

              <Database size={15} />

              <span>
                Expected Space
              </span>

              <strong>
                O(1)
              </strong>

            </div>

          </div>


        </section>


        {/* =========================
            RIGHT EDITOR
        ========================== */}

        <section className="editor-panel">


          {/* EDITOR HEADER */}

          <div className="editor-header">


            <div className="language-select">

              <select
                value={language}
                onChange={(e) =>
                  setLanguage(e.target.value)
                }
              >

                <option value="Java">
                  Java
                </option>

                <option value="JavaScript">
                  JavaScript
                </option>

                <option value="Python">
                  Python
                </option>

                <option value="C++">
                  C++
                </option>

              </select>

              <ChevronDown size={13} />

            </div>


            <span className="editor-status">
              Ready
            </span>

          </div>


          {/* MONACO */}

          <div className="monaco-wrapper">

            <Editor
              height="100%"
              language={
                language === "JavaScript"
                  ? "javascript"
                  : language === "C++"
                  ? "cpp"
                  : language.toLowerCase()
              }
              theme="vs-dark"
              value={code}
              onChange={(value) =>
                setCode(value || "")
              }
              options={{
                minimap: {
                  enabled: false,
                },

                fontSize: 13,

                padding: {
                  top: 15,
                },

                automaticLayout: true,

                scrollBeyondLastLine: false,

                tabSize: 4,

                wordWrap: "on",
              }}
            />

          </div>


          {/* RESULT */}

 {runResult && (

  <div
    className={`execution-result ${
      runResult.status === "Success" ||
      runResult.status === "Accepted"
        ? "success"
        : "error"
    }`}
  >

    {runResult.status === "Success" ||
     runResult.status === "Accepted" ? (
      <CheckCircle2 size={15} />
    ) : (
      <Clock3 size={15} />
    )}

    <div>

      <strong>
        {runResult.status}
      </strong>

      <pre>
        {runResult.output}
      </pre>

    </div>

  </div>

)}


          {/* EDITOR FOOTER */}

          <div className="editor-footer">



            <button
  className="run-button"
  onClick={handleRun}
  disabled={running}
>
  <Play size={14} />

  {running ? "Running..." : "Run"}

</button>


            <button
              className="submit-button"
              onClick={handleSubmit}
            >


              <Send size={14} />

              Submit

            </button>

          </div>


        </section>

      </div>

    </div>
  );
}


export default ProblemDetail;