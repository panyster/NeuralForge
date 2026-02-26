# test_neuralforge.py
"""
Tests for NeuralForge module.
"""

import unittest
from neuralforge import NeuralForge

class TestNeuralForge(unittest.TestCase):
    """Test cases for NeuralForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeuralForge()
        self.assertIsInstance(instance, NeuralForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeuralForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
