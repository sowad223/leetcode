Can you solve this real interview question? Regular Expression Matching - Given an input string s and a pattern p, implement regular expression matching with support for &#x27;.&#x27; and &#x27;*&#x27; where:

 * &#x27;.&#x27; Matches any single character.
 * &#x27;*&#x27; Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

 

Example 1:


Input: s = &quot;aa&quot;, p = &quot;a&quot;
Output: false
Explanation: &quot;a&quot; does not match the entire string &quot;aa&quot;.


Example 2:


Input: s = &quot;aa&quot;, p = &quot;a*&quot;
Output: true
Explanation: &#x27;*&#x27; means zero or more of the preceding element, &#x27;a&#x27;. Therefore, by repeating &#x27;a&#x27; once, it becomes &quot;aa&quot;.


Example 3:


Input: s = &quot;ab&quot;, p = &quot;.*&quot;
Output: true
Explanation: &quot;.*&quot; means &quot;zero or more (*) of any character (.)&quot;.


 

Constraints:

 * 1 &lt;= s.length &lt;= 20
 * 1 &lt;= p.length &lt;= 20
 * s contains only lowercase English letters.
 * p contains only lowercase English letters, &#x27;.&#x27;, and &#x27;*&#x27;.
 * It is guaranteed for each appearance of the character &#x27;*&#x27;, there will be a previous valid character to match.