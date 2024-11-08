---
title: "Licensing model that inherits the licensing of the original data"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


What you're referring to is ensuring that your **derivative dataset** inherits the same licensing terms as the original data you based it on. The ability to impose this depends on the original dataset's license, as some licenses explicitly require derivative works to carry the same or compatible licensing.

Here’s how you can approach this:

### 1. **Check the Original License Terms**:
The first step is to determine what license the original dataset is published under. Many licenses specify terms for derivatives, such as:
- Whether derivative works are allowed.
- Whether they must carry the same license (a copyleft provision).
- Whether the original dataset needs to be credited.

### Common Licensing Scenarios:
#### A. **If the Original License is Copyleft (e.g., CC BY-SA, ODbL)**
   - If the original data is licensed under a **copyleft** license, such as **Creative Commons Attribution-ShareAlike (CC BY-SA)** or **Open Database License (ODbL)**, then **you are required** to release your derivative dataset under the same license.
   - For example:
     - **Original License**: CC BY-SA 4.0
     - **Derivative License**: Must also be CC BY-SA 4.0.
   - This ensures the licensing terms remain the same for all future users.

#### B. **If the Original License is Permissive (e.g., CC BY, MIT License)**
   - If the original dataset is under a **permissive** license, such as **Creative Commons Attribution (CC BY)** or **MIT**, you are generally free to publish the derivative work under the same or a different license.
   - However, **you can choose** to maintain the original license for the sake of consistency. In this case, simply apply the same license to your dataset.

#### C. **If the Original License is Non-Commercial (e.g., CC BY-NC)**
   - If the original data was licensed under a **non-commercial** license, like **CC BY-NC**, any derivative dataset must also carry the same non-commercial restriction.
   - For example:
     - **Original License**: CC BY-NC 4.0
     - **Derivative License**: Must also be CC BY-NC 4.0.

### 2. **How to Apply the Original License to Your Derivative Dataset**:
Once you've determined the license of the original dataset, you can take steps to ensure your derivative dataset follows the same licensing terms.

#### A. **Include a License File**:
   - Create a `LICENSE` file in your dataset repository (e.g., on GitHub or in the root directory of your dataset).
   - Clearly state that the dataset is licensed under the same terms as the original and reference the original dataset's license.
   - **Example (for CC BY-SA 4.0)**:
     ```plaintext
     This dataset is a derivative work of [Original Dataset Name], licensed under [Original License Name].
     As required by the original license, this dataset is also licensed under [Original License Name] (CC BY-SA 4.0).
     ```
   - If the original dataset requires attribution, make sure to include proper attribution to the original dataset in this file.

#### B. **Document the License in Your Metadata or README**:
   - In your `README.md` or `dataset-metadata.json`, specify that the dataset inherits the original license.
   - **Example (for CC BY 4.0)**:
     ```markdown
     ## License
     This dataset is based on data from [Original Dataset Name], which is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
     As a derivative work, this dataset is also licensed under CC BY 4.0.
     ```

### 3. **Licenses to Look for**:
   - **CC BY-SA 4.0** (ShareAlike): Requires you to license derivative works under the same terms.
   - **ODbL**: Requires derivative databases to also be licensed under ODbL.
   - **CC BY 4.0** (Attribution): Allows flexibility but requires attribution to the original data.
   - **CC BY-NC 4.0** (Attribution-NonCommercial): Restricts commercial use and requires attribution in derivatives.

### 4. **If No License Is Provided with the Original Data**:
   - If the original dataset doesn’t specify a license, it’s best to avoid publishing derivative works unless you have explicit permission from the data owner, as you could run into legal or copyright issues.

### Conclusion:
If you want to ensure that your derivative dataset follows the same terms as the original dataset, you should:
1. Review the original dataset’s license.
2. Apply the same license to your derivative dataset.
3. Clearly document this in your repository’s `LICENSE` file or `README.md` to ensure that future users are aware of the inherited license.

Would you like help drafting a specific license statement for your dataset based on the original data’s license?